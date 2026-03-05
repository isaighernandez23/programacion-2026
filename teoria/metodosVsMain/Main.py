''' 
Created on March, 2026
@author: isaighernandez

'''
from Menu import *
class Main:
  pass
cuenta1 = Cuenta(3000, "AHORRO", "01/01/2023")
menu = Menu("BIENVENIDO")

menu.dar_bienvenida()

eleccion = menu.desplegar_menu()

menu.procesar_opciones(eleccion, cuenta1)