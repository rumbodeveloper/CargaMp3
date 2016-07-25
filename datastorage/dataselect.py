#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#
#Author: Rumbo181
#
#Date: '24/7/16'

'''Este modulo selecciona los archivos que se van a cargar'''

import random
from .datastorage import get_data_base


def select_files(to_load):
    '''
    Esta funcion gestiona la eleccion de ficheros a cargar, dado un volumen objetivo
    '''

    indices = _desordena()
    filenames_de_canciones = _acumulado_hasta(indices,to_load)
    return filenames_de_canciones


def _desordena():
    songs = get_data_base()
    indices = list(songs.keys())
    for n in range (3): #desordenamos muy desordenado
        random.shuffle(indices)
    return indices

def _acumulado_hasta(indices, to_load):
    '''
    Esta funcion devuelve la lista de los filenames hasta el volumen indicado por to_load

    '''

    songs = get_data_base()

    lista_de_indices_de_canciones = [] # aqui pondremos la lista de los indices de los ficheros a buscar
    volumen_acumulado = 0 # aqui pondremos el volumen acumulado

    # aqui escogemos los ficheros cuya suma de volumen esta por debajo de cierto limite
    for i in indices:
        volumen_acumulado += songs[i][1]  # acumulamos el volumen de los ficheros que cargamos
        if  volumen_acumulado > to_load:
            break
        lista_de_indices_de_canciones.append(i)


    lista_de_indices_de_canciones.sort()  # los ordenamos para que sea mas facil acceder al disco duro

    # preparamos la lista de nombres de ficheros a copiar
    filenames_de_canciones = [(songs[i][0],songs[i][1]) for i in lista_de_indices_de_canciones]

    return filenames_de_canciones

