import pandas as pd
import mysql.connector
import os
import re
import numpy as np
def upload():
    # Ruta absoluta del archivo CSV
    absolute_path = os.path.abspath('posts.csv')

    # Lectura del archivo CSV
    # Leer el archivo CSV y omitir las líneas con errores
    df = pd.read_csv(absolute_path, on_bad_lines='skip')
    df['URL_clean'] = df['URL_post'].str.split('?').str[0]

    # Eliminar duplicados en función de la columna "URL_clean"
    df = df.drop_duplicates(subset="URL_clean", keep="last")

    df = df.replace('', np.nan)  # Reemplazar los valores NaN po
    df = df.fillna(0)
    df = df.drop(columns=['URL_clean'])

    database_type = 'mysql'
    user = 'Facebook_user'
    password = 'user_facebook123'
    host = 'rimgsa.com'
    database_name = 'practicas_facebook_scrapper'
    
    db_connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database_name
    )

    # Creación del cursor
    cursor = db_connection.cursor()

    # Eliminación de los registros existentes en la tabla
   # delete_records_query = 'DELETE FROM clientes_facebook'
    #cursor.execute(delete_records_query)

    # Inserción de los datos del DataFrame en la tabla
    insert_records_query = '''
    INSERT INTO clientes_facebook (Nombre_pagina, URL_post, Recuento_compartidos, Reacciones_totales, Recuento_comentarios, Contenido, Fecha_hora_publicacion, Fecha, Hora,Estado)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    records = df.values.tolist()
    cursor.executemany(insert_records_query, records)

    # Confirmar los cambios y cerrar la conexión
    db_connection.commit()
    cursor.close()
    db_connection.close()

upload()