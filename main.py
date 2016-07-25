#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#
#Author: Rumbo181
#
#Date: '24/7/16'

'''Este modulo organiza la accion de los otros modulos del programa'''

import userinteface
import devicehandling
import datastorage
from configuration import *



def parada_forzada():
    raise Exception("PARADA FORZADA POR EL USUARIO")




def main():

    # Bienvenida y muestra de lo que hace el programa
    welcome="Bienvenido \n Este programa copia ficheros de muscia aleatoriamente de"\
    "\n {} a {},"\
    "\n borrando primero los que hubiere en {} \n".format(SOURCE_DIRECTORY,TARGET_DIRECTORY,TARGET_DIRECTORY)
    userinteface.show_title(welcome)

    #comprobacion de que el device esta connectado
    while not devicehandling.device_connected():

        prompt="Que quieres hacer?"
        opciones=[('Conectar el aparato que falta:',1),( "Salir: ",'q')]
        # aqui damos oportunidad a conectar el aparato que falta o a interrumpir el programa
        respuesta = userinteface.show_options(opciones=opciones,prompt= prompt,pregunta='')
        print(respuesta)
        if respuesta == 'q': parada_forzada()

    #preguntamos si queremos acutalizar la base de datos de canciones.
    pregunta="Quieres actualizar las canciones (esto llevara tiempo)?"
    prompt = "Que quieres hacer?"
    opciones=[('No quiero actualizar', 1),('Si, actualiza aunque lleve tiempo',99 ), ('Salir: ','q')]
    #aqui damos la oportunidad de actualizar la base de datos si es necesario
    respuesta = userinteface.show_options(opciones=opciones,prompt=prompt,pregunta=pregunta)
    if respuesta == 'q': parada_forzada()
    if respuesta == '99' : datastorage.update_songs()

    # inicializamos los datos
    datastorage.init()#esto carga la base de datos en el programa

    # preguntamos cuanta cantidad vamos a cargar
    pregunta = "Cuanta cantidad quieres cargar, entre {} y {} Gbytes: ".format(MIN_TO_LOAD,MAX_TO_LOAD)
    toload = userinteface.prompt_for_quantity(pregunta,min=MIN_TO_LOAD,max=MAX_TO_LOAD) #pregunta cuanto hay que cargar
    toload = toload * RATE_FROM_BYTES_TO_GIGABYTES # convertimos el dato en bytes

    # preguntamos si vamos a borrar lo que ya habia o simplemente lo vamos a agregar
    pregunta = "Quieres borrar lo que hay en el aparato de destino o prefieres conservarlo?"
    prompt = "Que quiere hacer "
    opciones = [('Borrar todo lo que hay ahora',1),('Dejar lo que ya hay',99), ('Salir', 'q'),]
    accion = userinteface.show_options(opciones=opciones,prompt=prompt,pregunta=pregunta)
    if accion == 'q': parada_forzada() #detenemos el programa
    if accion == '1': devicehandling.detele_target_files() # borramos los ficheros que habia en el destino



    # obtenemos la lista de los ficheros a cargar
    files_to_load = datastorage.select_files(toload)


    # cargamos los ficheros en el aparato objetivo
    devicehandling.load_files(files_to_load)# carga los ficheros en el device

    # mostramos que el programa ha terminado
    userinteface.show_title("PROGRAMA TERMINADO")#muestra el mensaje de que ya se ha terminado la actualizacion









if __name__ == "__main__":
    main()