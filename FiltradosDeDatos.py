import pandas as pd
import os
import datetime
from datetime import datetime
import shutil

# Ruta de la carpeta
CARGA_DE_ARCHIVOS = os.path.expanduser("~/Desktop/Carga de archivos")

# Revisa la existencia de una carpeta y si no existe la crea
if os.path.exists(CARGA_DE_ARCHIVOS):
    print("Carpeta de archivos existente")
else: 
    try:
        os.mkdir(CARGA_DE_ARCHIVOS)
        print("Carpeta de archivos Creada")
    except OSError as error:
        print(f"No se pudo crear la carpeta")

RUTA_ORIGINAL = os.path.expanduser(r"~\Downloads\descargas\orders_export.csv")

RUTA_DESTINO = os.path.expanduser(r"~/Desktop/Carga de archivos/orders_export.csv")

# Revisa si un archivo existe y lo mueve a una direccion especificada
if os.path.exists(RUTA_ORIGINAL):
    try:
        shutil.move(RUTA_ORIGINAL,RUTA_DESTINO)
        print("Archivo orders_export movido correctamente")
    except OSError as error:
        print("Archivo orders_export no movido")
else:
    print("Archivo orders_export no existe")

# Ruta del archivo a modificar
RUTA_ARCHIVO = os.path.expanduser("~/Desktop/Carga de archivos/orders_export.csv")

# Cargar el archivo CSV existente en un DataFrame
archcsv1 = pd.read_csv(RUTA_ARCHIVO)

# Seleccionar las columnas de interés y crear una copia del DataFrame
columnas_a_copiar = archcsv1[['Created at', 'Name', 'Billing Name', 'Lineitem quantity', 'Lineitem name', 'Shipping Province Name', 'Billing Street','Shipping Phone']].copy()

# Remover la zona horaria (-0400) de los valores en la columna 'Created at'
columnas_a_copiar['Created at'] = columnas_a_copiar['Created at'].str[:-6]

# Convertir a datetime
columnas_a_copiar['Created at'] = pd.to_datetime(columnas_a_copiar['Created at'], format='%Y-%m-%d %H:%M:%S')

# Formatear la fecha como 'dd-mm-YYYY'
columnas_a_copiar['Created at'] = columnas_a_copiar['Created at'].dt.strftime('%d/%m/%Y')

# Calcular el número de filas en el DataFrame original
num_filas = len(archcsv1)

nueva_columna1 = [""] * num_filas
nueva_columna2 = [""] * num_filas
nueva_columna3 = [""] * num_filas

# Definir las posiciones de las nuevas columnas
posicion_columna1 = 7
posicion_columna2 = 8
posicion_columna3 = 9

# Insertar las nuevas columnas en el DataFrame
columnas_a_copiar.insert(posicion_columna1, "Status", nueva_columna1)
columnas_a_copiar.insert(posicion_columna2, "NC2", nueva_columna2)
columnas_a_copiar.insert(posicion_columna3, "NC3", nueva_columna3)

archcsv1['Shipping Company'] = archcsv1['Shipping Company'].replace(".","")
archcsv1['Shipping Company'] = archcsv1['Shipping Company'].replace(" ","")

# Verificaciones y actualizaciones del dataframe columnas_a_copiar
for index, row in archcsv1.iterrows():
    if row['Financial Status'] == 'paid':
        if row['Shipping Company'].startswith("DNI "):
            pass
        else:
            if not row['Shipping Company'].isnumeric():
                columnas_a_copiar.loc[index, 'Status'] = "FALTA DNI"
    else:
        if row['Financial Status'] == 'pending':
            columnas_a_copiar.loc[index, 'Status'] = "FALTA PAGAR"
        else:
            pass

for index, row in archcsv1.iterrows():
    if row['Financial Status'] == 'paid':
        if row['Shipping Province Name'] == 'Ciudad Autónoma de Buenos Aires':
            columnas_a_copiar.loc[index, 'Status'] = "CABA"
    else:
        pass

# Esta es la copia que se almacena en Carga de archivos
ArchivoFinal = columnas_a_copiar

# Esta es la copia que se sube a Google Drive 
Dataframe_Final = columnas_a_copiar

# Acá se obtiene el día para agregarlo en el nombre del archivo
Fecha_arch = columnas_a_copiar.loc[0,'Created at']

Fecha_arch = Fecha_arch.replace('/','-')

Fecha_arch_datetime = datetime.strptime(Fecha_arch, '%d-%m-%Y')

Fecha = Fecha_arch_datetime.strftime('%d-%m-%y')

# Guardar el DataFrame modificado en otro archivo CSV con la fecha del día de los pedidos en el archivo
ArchivoFinal.to_csv(os.path.expanduser("~/Desktop/Carga de archivos/Archivo "+Fecha+".csv"), index=False)