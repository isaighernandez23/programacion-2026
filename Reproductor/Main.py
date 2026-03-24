''' 
Created on March, 2026
@author: isaighernandez23

'''
from Menu import *
from Playlist import *

class Main:
  pass

cancion1 = Cancion("Hola", "Isai", 5, "Hip-Hop")
cancion2= Cancion("i", "k",7,"Jazz")
cancion3= Cancion("M","T",6,"Rap")

playlist1=Playlist("Rolas",cancion1=cancion1,cancion2=cancion2,cancion3=cancion3)

print(playlist1)

