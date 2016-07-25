#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#
#Author: Rumbo181
#
#Date: '24/7/16'

from configuration import *
from userinteface import show_message, show_error
import os
import shutil


DEVICES = [SOURCE_DIRECTORY,TARGET_DIRECTORY]


def device_connected():
    ''' comprueba que todo esta conectado'''
    for dev in DEVICES:
        if not _connected(dev):
            show_message("El aparato {} no esta conectado  "\
                         "por favor conectale \n".format(dev))
            return False
    show_message("Correcto, todos los aparatos estan conectados \n")
    return True


def detele_target_files():
    '''
    esta funcion borra el contenido previo en el disco destino
    '''
    if not _delete_files():
        show_error("No ha sido posible borrar los ficheros que habia en el aparato destino")
    else:
        show_message("Contenido existente en el aparato destino borrado")


def load_files(list_of_files):
    '''
    Esta funcion gestiona la copia de ficheros e informa de como lo va haciendo
    '''

    ficheros_copiados = 0
    volumen_copiado = 0

    for i in list_of_files:
        volumen_copiado = volumen_copiado + i[1]/RATE_FROM_BYTES_TO_GIGABYTES # voy sumando el volumen
        if not _copia_fichero(i[0]): #aqui le decimos que copie el fichero
            show_error("Problema con el fichero {}, no se pudo copiar".format(i[0]))
        else:
            ficheros_copiados += 1
            show_message("Ficheros copiados {0:.0f} con un volumen de {1:.2f} Gbytes".format(ficheros_copiados,volumen_copiado))




def _delete_files():
    '''
    borra todo lo que hubiera en el fichero
    '''
    try:
        shutil.rmtree(TARGET_DIRECTORY)  # borro lo que haya, incluido el directorio
        if not os.path.exists(TARGET_DIRECTORY):  # chequeo que lo he borrado bien
            os.mkdir(TARGET_DIRECTORY)
        return True
    except:
        return False


def _connected(devicepath):
    if  not os.path.exists(devicepath):
        return False
    return True

def _copia_fichero(fichero):
    """
    esta funcion copia ficheros individuales
    """
    target = fichero
    destino = fichero.replace(SOURCE_DIRECTORY, TARGET_DIRECTORY)
    try:
        if not os.path.exists(os.path.dirname(destino)):
            os.makedirs(os.path.dirname(destino))
        with open(target, 'rb') as fsrc:
            with open(destino, 'wb') as fdst:
                for x in iter(lambda: fsrc.read(16384), ""):
                    fdst.write(x)

        return True
    except:
        return False