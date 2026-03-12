''' 
Created on March, 2026
@author: isaighernandez

'''
from Cancion import * 
class Menu:
  def __init__(self, mensaje):
    self.mensaje = mensaje

  def dar_bienvenida(self):
    print(self.mensaje)

  def desplegar_menu(self):
    print("¿QUÉ DESEAS HACER?:")
    print("1. CONSULTAR INFORMACIÓN DE LA CANCIÓN")
    print("2. REPRODUCIR")
    print("3. DETENER")
    print("4. SALIR")
    
    opciones = int(input("SELECCIONE UNA OPCIÓN: "))
    return opciones 

  def procesar_opciones(self, opciones, cancion1):
    if opciones == 1:
      print(cancion1.informacion_cancion())
  

    elif opciones == 2:
      cancion1.reproducir()

    elif opciones == 3:
      cancion1.pausar()

    elif opciones == 4:
      print("SALIENDO DEL REPRODUCTOR. ¡VUELVA PRONTO!")

    else:
      print("\nOPCIÓN NO VÁLIDA. INTENTA DE NUEVO.")


