import pandas as pd


def cargar_datos(ruta_csv: str, encoding: str = "utf-8", separador: str = ";") -> pd.DataFrame:
    """
    Carga un archivo CSV y lo devuelve como DataFrame.
    """
    return pd.read_csv(ruta_csv, encoding=encoding, sep=separador)


def manejar_valores_nulos(
    df: pd.DataFrame,
    estrategia: str = "drop",
    fill_values: dict | None = None,
) -> pd.DataFrame:
    """
    Maneja valores nulos (NaN).
    """
    df = df.copy()

    if estrategia == "drop":
        df = df.dropna()
    elif estrategia == "fill":
        if not fill_values:
            raise ValueError("Si estrategia='fill', debes pasar fill_values.")
        df = df.fillna(fill_values)
    else:
        raise ValueError("estrategia debe ser 'drop' o 'fill'.")

    return df


def estandarizar_texto(df: pd.DataFrame, columnas: list[str]) -> pd.DataFrame:
    """
    Convierte texto a minúsculas y elimina espacios extra.
    """
    df = df.copy()

    for col in columnas:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
                .str.lower()
            )

    return df


def limpiar_precio(df: pd.DataFrame, columna: str = "precio") -> pd.DataFrame:
    """
    Limpia la columna precio y la convierte a numérica.
    """
    df = df.copy()

    if columna in df.columns:
        df[columna] = (
            df[columna]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.strip()
        )
        df[columna] = pd.to_numeric(df[columna], errors="coerce")

    return df
