"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


import pandas as pd 
import os 

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd
    import os

    file_path = "./files/input/solicitudes_de_credito.csv"
    df = pd.read_csv(file_path, sep = ";")

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df.rename(columns={'Unnamed: 0': 'index'}, inplace=True)
    df.set_index('index', inplace=True)

    # Columna Sexo
    df.sexo = df.sexo.str.lower()
    df.sexo = df.sexo.astype('category')


    # Columna tipo_de_emprendimiento
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.astype('category')        

    # Columna idea_negocio
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio =df.idea_negocio.replace('-',' ', regex=True)
    df.idea_negocio =df.idea_negocio.replace('_',' ', regex=True)   
    df.idea_negocio = df.idea_negocio.str.strip()

    # Columna barrio

    df.barrio = df.barrio.str.lower().str.replace('_','-').str.replace("-", " ").str.strip()    

    # Columna comuna_ciudadano
    df.comuna_ciudadano = df.comuna_ciudadano.astype('Int64')
    df.comuna_ciudadano  = df.comuna_ciudadano.astype('category')

    # Columna fecha_de_beneficio
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True, format='mixed')

    # Columna monto_del_credito
    df.monto_del_credito = df.monto_del_credito.str.replace('$','').str.replace(',','')
    df.monto_del_credito = df.monto_del_credito.astype(float).astype(int)

    # Columna línea_credito
    df.línea_credito = df.línea_credito.str.lower().str.strip('_').str.strip('-').str.strip().str.replace('_',' ').str.replace('-', ' ') 
        

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    output_file = 'files/output'
    os.makedirs(output_file, exist_ok=True)

    output_path = f'{output_file}/solicitudes_de_credito.csv'
    df.to_csv(output_path, sep=';', index=False)     

    return df            