import pandas as pd


def cargar_datos(ruta_csv: str, encoding: str = "utf-8", separador: str = ";") -> pd.DataFrame:
    """
    Carga un archivo CSV y lo devuelve como DataFrame.
    """
    df = pd.read_csv(ruta_csv, encoding=encoding, sep=separador)
    return df

def estandarizar_texto(df: pd.DataFrame, columnas: list[str]) -> pd.DataFrame:
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
