from data_cleaning import cargar_datos

RUTA_CSV = "data/productos.csv"  # cambia el nombre si tu CSV se llama distinto

df = cargar_datos(RUTA_CSV)

print("Columnas:", list(df.columns))
print("\nPrimeras 5 filas:")
print(df.head())
print("\nFilas, Columnas:", df.shape)
