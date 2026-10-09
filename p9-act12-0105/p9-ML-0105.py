# Iker Montoya 0105
import pandas as pd
import numpy as np
import os

# Obtener la ruta exacta de la carpeta donde se encuentra este script
directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_local = os.path.join(directorio_script, "datos12.csv")

# Ruta de respaldo directa en GitHub
url_github = "https://raw.githubusercontent.com/Eliseo128/practicas-pandas-ML-2023/main/datos12.csv"

# Carga de datos con detección de ruta local o remota
if os.path.exists(ruta_local):
    print(f"Cargando archivo local desde: {ruta_local}\n")
    df_datos12 = pd.read_csv(ruta_local)
else:
    print("Archivo local 'datos12.csv' no encontrado. Intentando descargar desde GitHub...\n")
    try:
        df_datos12 = pd.read_csv(url_github)
    except Exception as e:
        print("Error: No se encontró 'datos12.csv' localmente ni en el repositorio.")
        print("Asegúrate de colocar 'datos12.csv' en la misma carpeta que este script.")
        raise e

# 1. Vista previa de los datos
print("--- Vista previa de datos12 ---")
print(df_datos12.head())

# 2. Información general de las columnas
print("\n--- Información general del DataFrame ---")
df_datos12.info()

# 3. Detección de valores nulos
print("\n--- Valores nulos por columna ---")
print(df_datos12.isnull().sum())

# 4. Estadísticas descriptivas generales
print("\n--- Estadísticas descriptivas ---")
print(df_datos12.describe())

# Impresión final
print("\nIker Montoya 0105")