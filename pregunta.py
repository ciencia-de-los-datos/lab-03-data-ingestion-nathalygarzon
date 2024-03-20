"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    #
    # Inserte su código aquí
    #

    with open("clusters_report.txt","r") as file:
        datos = file.readlines()

    datos = [linea.strip() for linea in datos]

    data_slice = datos[4:]

    patron = '^(\d+)\s+(\d+)\s+(\d+,\d+)[%\s]+(.+)'

    full_data = []
    lista = []
    text = ""

    for line in data_slice:
        result = re.search(patron, line)
        if result:
            lista = [int(result.group(1)), int(result.group(2)), float(result.group(3).replace(',','.'))]
            text = result.group(4)
        else:
            text = f"{text} {line}"
        
        if len(line) == 0:
            lista = lista + [text]
            full_data.append(lista)
            lista = []
            text = ""

    columnas = ["Cluster","Cantidad de palabras clave","Porcentaje de palabras clave","Principales palabras clave"]
    col = [column.lower().replace(" ","_") for column in columnas]

    df = pd.DataFrame(full_data, columns=col)
    df["principales_palabras_clave"] = df["principales_palabras_clave"].str.strip()
    df["principales_palabras_clave"] = df["principales_palabras_clave"].str.replace(".","")
    df["principales_palabras_clave"] = df["principales_palabras_clave"].str.replace(r"[ ]+"," ",regex=True)

    return df