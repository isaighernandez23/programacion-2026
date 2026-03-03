#Menú.py
from Cuenta import *
class Menu:
 def __init__(self, mensaje):
  self.mensaje = mensaje
 def dar_bienvenida(self):
  print(self.mensaje)
cuenta1 = Cuenta(3000, "Ahorro", "01/01/2023")
cuenta1.informacion() #no es necesario el print porque no regresa una cadena#eel 
#self en e lcodigo anterior significa vacío en este otro archivo

#--------------------------------------------------------------------------------
menu = Menu("hola")
menu.dar_bienvenida()
ingresar_cuenta = str(input("ingrese su cuenta:"))
opciones = int(input( "¿Qué desea hacer? 1. Retirar 2. Depositar 3. Informacion:"))
if opciones == 1 :
  c = float(input("ingrese la cantidad a retirar:"))
  cuenta1.retirar(c)
  print("Su nuevo saldo es:",cuenta1.saldo)
elif opciones == 2 :
  c = float(input("ingrese la cantidad a depositar:"))
  cuenta1.depositar(c)
  print("Su nuevo saldo es",cuenta1.saldo)
elif opciones == 3 :
  cuenta1.informacion()
    