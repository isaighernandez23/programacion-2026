''' 
Created on March, 2026
@author: isaighernandez

'''
from Menu import *
class Main:
  pass

cancion1 = Cancion("Hola", "Isai", 5, "Hip-Hop")

menu = Menu("=== BIENVENIDO A TU BIBLIOTECA MUSICAL ===")

menu.dar_bienvenida()

eleccion = menu.desplegar_menu()

menu.procesar_opciones(eleccion, cancion1)
