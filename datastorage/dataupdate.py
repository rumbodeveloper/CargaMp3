#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#
#Author: Rumbo181
#
#Date: '24/7/16'

'''
Este modulo comprueba si existen actualizaciones
'''

from userinteface import show_message,show_error
from configuration import *
import json
import os


def update_songs():
    '''
    actualizo la lista de nombres de ficheros de las canciones y la guardo en un fichero
    la estructura del diccionario es
    key: un numero secuencial
    value: una tupla, con el nombre del fichero completo en posicion [0] y su volumen en
    posicion [1]

    '''


    all_files = []# lista inicial

    for path, dir, listfiles in os.walk(SOURCE_DIRECTORY): #escaneo el directorio
        file_list=[(os.path.join(path,f), os.path.getsize(os.path.join(path,f)))
                 for f in listfiles if f.endswith('.mp3')]

        if not file_list: # para no procesar nada si la lista obtenida esta vacia
            continue

        all_files = all_files + file_list
        show_message("Agregados {} ficheros".format(len(all_files)))

    canciones = {k: f for k, f in enumerate(all_files)} #creo un diccionario
    show_message("Creado un diccionario con los ficheros")
    try:
        with open (SONGS_NAMES_FILE,"w")as file:
            file.write(json.dumps(canciones))
            show_message("PROCESO DE ACTUALIZACION TERMINADO \n")
    except:
        show_error("Algo fallo guardando el fichero con los datos de los ficheros")



