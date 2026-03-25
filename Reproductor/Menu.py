
     ''' 
Created on March, 2026
@author: isaighernandez

'''
from Cancion import * 
from Playlist import *

class Menu:
  def __init__(self, mensaje):
    self.mensaje = mensaje

  def dar_bienvenida(self):
    print(self.mensaje)

  def desplegar_menu(self):
    print("¿QUÉ DESEAS HACER?:")
    print("1. CONSULTAR INFORMACIÓN DE LA CANCIÓN")
    print("2. REPRODUCIR CANCION")
    print("3. DETENER CANCION")
    print("4. REPRODUCIR PLAYLIST")
    print("5. SALIR")
    opciones = int(input("SELECCIONE UNA OPCIÓN: "))
    return opciones 

  def procesar_opciones(self, opciones, cancion1,playlist1):
    if opciones == 1:
      print(cancion1)
    
    elif opciones == 2:
      print(cancion1.reproducir())

    elif opciones == 3:
      print(cancion1.pausar())

    elif opciones== 4:
      print(playlist1.reproducir())
      
    elif opciones == 5:
      print("SALIENDO DEL REPRODUCTOR. ¡VUELVA PRONTO!")

    else:
      print("OPCIÓN NO VÁLIDA. INTENTA DE NUEVO.")





