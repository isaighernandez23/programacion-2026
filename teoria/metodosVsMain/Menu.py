''' 
Created on March, 2026
@author: isaighernandez

'''
from Cuenta import *
class Menu:
 def __init__(self, mensaje):
   self.mensaje = mensaje
 def desplegar_menu():
  print("¿QUE DESEAS HACER?:")
  print("1. CONSULTAR INORMACION")
  print("2. RETIRAR")
  print("3.  DEPOSITAR ")
  print("4. SALIR")

 def dar_bienvenida(self):
  print(self.mensaje)



 def desplegar_menu(self):
  print("¿QUE DESEAS HACER?:")
  print("1. CONSULTAR INORMACION")
  print("2. RETIRAR")
  print("3.  DEPOSITAR ")
  print("4. SALIR")
  
  opciones = int(input("SELECCIONE UNA OPCION:"))
  return opciones 

 def procesar_opciones(self,opciones,cuenta1):
  if opciones == 1 :
    c = float(input("INGRESE LA CANTIDAD A RETIRAR:"))
    cuenta1.retirar(c)
    print("SU NUEVO SALDO ES:",cuenta1.saldo)

  elif opciones == 2 :
    c = float(input("INTRESE LA CANTIDAD A DEPOSITAR:"))
    cuenta1.depositar(c)
    print("SU NUEVO SALDO ES:",cuenta1.saldo)

  elif opciones == 3 :
    cuenta1.informacion()

  elif opciones == 4:
    print("VUELVA PRONTO")
    
  
  
class Main:
  pass
cuenta1 = Cuenta(3000, "AHORRO", "01/01/2023")
menu = Menu("BIENVENIDO")

menu.dar_bienvenida()

eleccion = menu.desplegar_menu()

menu.procesar_opciones(eleccion, cuenta1)


  

    