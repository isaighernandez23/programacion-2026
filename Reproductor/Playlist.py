''' 
Created on March, 2026
@author: isaighernandez
'''
from Cancion import *
class Playlist:
    def __init__(self, nombre_playlist,cancion1, cancion2,cancion3):
        self.nombre_playlist=nombre_playlist
        self.cancion1=cancion1
        self.cancion2=cancion2
        self.cancion3=cancion3
    
    def __str__(self):
        tmp = "Nombre de la playlist::" + str(self.nombre_playlist)
        tmp += "\nCanción 1::" + str(self.cancion1)
        tmp += "\nCanción 2::" + str(self.cancion2)
        tmp += "\nCanción 3::" + str(self.cancion3)
        return tmp
   
