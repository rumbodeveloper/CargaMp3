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

    global _songs_dict
    _songs_dict={}

    # detecto si esta el fichero y si esta lo cargo

    try:
        with open(SONGS_NAMES_FILE, "r") as file: # y si existe lo cargo
            print("Existe el fichero de canciones - lo cargo")
            _songs_dict = json.loads(file.read())
            print("Tiene {} canciones. ".format(len(_songs_dict)))
    except:
        pass

    contador_canciones_nuevas = 0
    contador_actividad = 0

    canciones_existentes=list( _songs_dict.keys())
    print("numero de claves en el diccionario: {}".format(len(set(_songs_dict.keys()))))


    for path, dir, listfiles in os.walk(SOURCE_DIRECTORY): #escaneo el directorio
        contador_actividad += 1
        print("Scaneando: actividad {}".format(contador_actividad))
        for f in listfiles:
            if f.endswith('.mp3'):
                fichero_y_su_path=os.path.join(path,f)
                if  not fichero_y_su_path in canciones_existentes:
                    contador_canciones_nuevas += 1
                    canciones_existentes.append(fichero_y_su_path)
                    _songs_dict[fichero_y_su_path]=(fichero_y_su_path, os.path.getsize(fichero_y_su_path))
                    show_message("Agregadas {} canciones".format(contador_canciones_nuevas))

    show_message("Actualizado  un diccionario con los ficheros")
    try:
        with open (SONGS_NAMES_FILE,"w")as file:
            file.write(json.dumps(_songs_dict))
            show_message("PROCESO DE ACTUALIZACION TERMINADO \n")
    except:
        show_error("Algo fallo guardando el fichero con los datos de los ficheros")



