
''' 
Created on March, 2026
@author: isaighernandez

'''
from Playlist import *
from Cancion import Cancion
class Usuario:
    def __init__(self,usuario,correo, contraseña):
        self.usuario=usuario
        self.__correo=correo # 
        self.__contraseña=contraseña 
        self.playlists=[]  # un usuario puede tener muchas playlists
        self.favoritas=[]  # un usuario puede tener muchas canciones favoritas
        self.biblioteca=[] # todas las canciones del usuario

    def agregar_playlist(self, playlists):
        self.playlists.append(playlists)

    def agregar_favorita(self, cancion):
        self.favoritas.append(cancion)

    def agregar_biblioteca(self,cancion):
        self.biblioteca.append(cancion)

    def mostrar_biblioteca(self):
     print(f"========== Canciones ==========")

     if len(self.biblioteca) == 0:
        print("La Biblioteca está vacía actualmente")

     else:
        i = 1
        for cancion in self.biblioteca:
            print(f"{i}. {cancion.titulo} - {cancion.artista} [{cancion.genero}]")
            i += 1