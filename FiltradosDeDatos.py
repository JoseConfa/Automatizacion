import pandas as pd
import os

ARCHCSV1 = pd.read_csv("C:/Users/Jose/Desktop/Carga de archivos/orders_export.csv")

columnas_a_copiar = ARCHCSV1[['Billing Name','Billing Phone','Lineitem quantity','Lineitem name','Billing Street','Total']].copy()

columnas_a_copiar.to_csv("C:/Users/Jose/Desktop/Carga de archivos/Archivo listo.csv", index=False)

num_filas = len(ARCHCSV1)

nueva_columna1 = [","] * num_filas
nueva_columna2 = [","] * num_filas
nueva_columna3 = [","] * num_filas
nueva_columna4 = [","] * num_filas
nueva_columna5 = [","] * num_filas

posicion_columna1 = 1
posicion_columna2 = 3
posicion_columna3 = 5
posicion_columna4 = 7
posicion_columna5 = 9

columnas_a_copiar.insert(posicion_columna1, "NuevaColumna1", nueva_columna1)
columnas_a_copiar.insert(posicion_columna2, "NuevaColumna2", nueva_columna2)
columnas_a_copiar.insert(posicion_columna3, "NuevaColumna3", nueva_columna3)
columnas_a_copiar.insert(posicion_columna4, "NuevaColumna4", nueva_columna4)
columnas_a_copiar.insert(posicion_columna5, "NuevaColumna5", nueva_columna5)


columnas_a_copiar.to_csv("C:/Users/Jose/Desktop/Carga de archivos/Archivo Final.csv", index=False)


archivo_csv = "C:/Users/Jose/Desktop/Carga de archivos/Archivo listo.csv"

# Verificar si el archivo existe
if os.path.exists(archivo_csv):
    # Eliminar el archivo
    os.remove(archivo_csv)
    print("Archivo CSV eliminado con éxito.")
else:
    print("El archivo CSV no existe.")

