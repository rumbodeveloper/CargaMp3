#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#
#Author: Rumbo181
#
#Date: '24/7/16'

'''
Este modulo contiene las interfaces de comunicacion con el usuario
'''





def show_message(texto):
    ''' esta funcion imprime un mensaje'''
    print(texto)

def show_error(texto):
    '''esta funcion imprime un error'''
    print(50 * '-')
    print(texto)
    print(50 * '-')
    print()

def show_title(texto):
    '''
    esta funcion muestra el titulo del programa
    '''
    print(50 * '=')
    print(texto)
    print(50 * '=')
    print()

def show_options(opciones,prompt, pregunta):
    '''
    gestiona que el usuario escoja entre opciones
    :param opciones: es una lita de tuplas, cada tupla tiene [0] opcion y [1] valor
    :param prompt: es que pregunta el input
    :param pregunta: es una pregunta generica que se hace al principio
    :return:
    '''
    if type(pregunta) is str:
        print(pregunta.capitalize(),'\n',)
    [print(i[0],'\t',i[1]) for i in opciones]
    valores = [str(i[1]) for i in opciones]
    while True:
        valor = input(prompt)
        if valor not in valores: print("Respuesta no valida \n")
        else: return valor


def prompt_for_quantity(question,min,max):
    while True:
        print()
        try:
            cantidad = input(question)
            cantidad = float(cantidad)
            if (cantidad >= min) & (cantidad <= max):
                return float(cantidad)
        except:
            print("Revisa lo que has contestado, algo falla")

