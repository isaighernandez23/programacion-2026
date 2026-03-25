''' 
Created on March, 2026
@author: isaighernandez

'''
from Cancion import *
from Menu import *
from Playlist import *

class Main:
  pass

cancion1 = Cancion("Hola", "Isai", 5, "Hip-Hop")
cancion2= Cancion("i", "k",7,"Jazz")
cancion3= Cancion("M","T",6,"Rap")

playlist1=Playlist("Rolas",cancion1,cancion2)


menu = Menu("=== BIENVENIDO A TU BIBLIOTECA MUSICAL ===")

menu.dar_bienvenida()

eleccion = menu.desplegar_menu()

menu.procesar_opciones(eleccion, cancion1,playlist1)
