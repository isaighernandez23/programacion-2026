''' 
Created on March, 2026
@author: isaighernandez
'''
from Cancion import *
class Playlist:
    def __init__(self,nombre_playlist):
      self.nombre_playlist = nombre_playlist
      self.canciones=[]
      self.reproduciendo=False
    
    def reproducir(self):
       self.reproduciendo = True
       return f"REPRODUCIENDO:{self.nombre_playlist}"
    
    def __str__(self):
        print(f"========== PLAYLIST: {self.nombre_playlist} ==========")
        if len(self.canciones) == 0:
            print("La Playlist esta vacia actualmente")
        else:
           i = 1
           for titulo in self.canciones:
             print(i,titulo)
             i+= 1
    
    def añadir_cancion(self,titulo):
        if len(self.canciones) >= 500:
          print("La Playlist está llena")
        else:
          if titulo in self.canciones:
           print(f"{titulo} ya se encuentra en {self.nombre_playlist}")
          else:
            self.canciones.append(titulo)
          print(f"{titulo} añadida a {self.nombre_playlist}.")
  

    def buscador(self,texto):
      busqueda= texto.upper().strip()
      for  cancion in self.canciones:
        if busqueda in cancion.titulo.upper():
         print(f"LA CANCION {busqueda} FORMA PARTE DE LA PLAYLIST:{self.nombre_playlist}")
         break
      else:
         print(f"LA CANCION {busqueda} NO EXISTE EN LA PLAYLIST {self.nombre_playlist}")