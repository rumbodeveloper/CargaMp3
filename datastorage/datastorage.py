#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#
#Author: Rumbo181
#
#Date: '24/7/16'

from configuration import *
from .dataupdate import update_songs
import json
import os


def init():
    '''
    Comprobamos si existe el fichero donde guardamos los nombres de los ficheros
    de las canciones
    Si existe lo cargamos.
    Si no existe lo creamos con una actualizacion
    '''
    global _songs_dict #inicializamos la variable donde van los nombres de los ficheros

    if not os.path.exists(SONGS_NAMES_FILE): #si no existe el fichero lo creo
        update_songs()

    with open(SONGS_NAMES_FILE, "r") as file: # y si existe lo cargo
        _songs_dict = json.loads(file.read())


def get_data_base():
    global _songs_dict
    return _songs_dict