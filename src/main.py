from data_cleaning import (
    cargar_datos,
    manejar_valores_nulos,
    estandarizar_texto,
    limpiar_precio,
)

RUTA_CSV = "data/productos.csv"

# 1) Cargar y limpiar
df = cargar_datos(RUTA_CSV)
df = manejar_valores_nulos(df, estrategia="drop")
df = estandarizar_texto(df, ["producto", "categoria"])
df = limpiar_precio(df, "precio")

print("✅ Dataset limpio. Filas:", len(df))
print(df.head())

# -----------------------------
# A) FILTRADO
# -----------------------------
df_gadgets = df[df["categoria"] == "gadgets"]
print("\n[A] Filtrado: ¿cuántos son gadgets?")
print("Total gadgets:", len(df_gadgets))

# -----------------------------
# B) MERGE (ejemplo real)
# Creamos una tabla de categorías con un "impuesto" y la unimos al df
# -----------------------------
impuestos = {
    "gadgets": 0.19,
    "electronica": 0.16,
}

df_cat = (
    df[["categoria"]]
    .drop_duplicates()
    .assign(impuesto=lambda x: x["categoria"].map(impuestos).fillna(0.10))
)

df_merge = df.merge(df_cat, on="categoria", how="left")
df_merge["precio_con_impuesto"] = df_merge["precio"] * (1 + df_merge["impuesto"])

print("\n[B] Merge: columnas nuevas -> impuesto, precio_con_impuesto")
print(df_merge[["producto", "categoria", "precio", "impuesto", "precio_con_impuesto"]].head())

# -----------------------------
# C) GROUPBY (preguntas clave)
# -----------------------------
print("\n[C] GroupBy: resumen por categoría (conteo, total, promedio)")
resumen = (
    df_merge.groupby("categoria")["precio"]
    .agg(conteo="count", total="sum", promedio="mean", maximo="max", minimo="min")
    .sort_values(by="total", ascending=False)
)
print(resumen)

print("\n[C2] Top 3 productos más caros:")
top3 = df_merge.sort_values(by="precio", ascending=False).head(3)[["producto", "categoria", "precio"]]
print(top3.to_string(index=False))
