''' 
Created on March, 2026
@author: isaighernandez
'''
from Cancion import *
class Playlist:
    def __init__(self, nombre_playlist,cancion1, cancion2):
        self.nombre_playlist=nombre_playlist
        self.cancion1=cancion1
        self.cancion2=cancion2
        self.reproduciendo=False
    
    def reproducir(self):
       self.reproduciendo = True
       return f"REPRODUCIENDO:{self.nombre_playlist}"
    
    def __str__(self):
        tmp = "Nombre de la playlist::" + str(self.nombre_playlist)
        tmp += "\nCanción 1::" + str(self.cancion1)
        tmp += "\nCanción 2::" + str(self.cancion2)
        return tmp
    
