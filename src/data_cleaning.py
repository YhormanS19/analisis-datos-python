import pandas as pd


def cargar_datos(ruta_csv: str, encoding: str = "utf-8", separador: str = ";") -> pd.DataFrame:
    """
    Carga un archivo CSV y lo devuelve como DataFrame.
    """
    df = pd.read_csv(ruta_csv, encoding=encoding, sep=separador)
    return df
