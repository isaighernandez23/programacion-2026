''' 
Created on March, 2026
@author: isaighernandez

'''
class Cuenta:
  def __init__(self, saldo, tipo, fecha_creacion):
    self.saldo = saldo
    self.tipo = tipo
    self.fecha_creacion = fecha_creacion
  
  def __str__(self):
   return f"Cuenta {self.tipo}  Saldo: ${self.saldo} Fecha de Creacion: {self.fecha_creacion}"

  def retirar(self, cantidad):
    if cantidad> self.saldo:
      return False
    self.saldo = self.saldo - cantidad
    return True

  def depositar(self, cantidad):
    if cantidad <= 0:
      return False
    self.saldo = self.saldo + cantidad
    return True 
  
 
 



 
  