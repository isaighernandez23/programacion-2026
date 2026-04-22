''' 
Created on March, 2026
@author: isaighernandez

'''
from Cuenta import * 
class Cliente:
    def __init__(self,nombre,cuenta,direccion,fecha_nacimiento):
        self.nombre=nombre
        self.cuenta=cuenta
        self.direccion=direccion
        self.fecha_nacimiento=fecha_nacimiento

        
    def __str__(self):
        return f"Cliente: {self.nombre} Fecha de Nacimiento: {self.fecha_nacimiento} Direccion: {self.direccion} Detalles de la Cuenta: {self.cuenta}"     