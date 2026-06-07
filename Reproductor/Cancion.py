''' 
Created on May, 2026
@author: isaighernandez

'''
from Archivo import Archivo
class Cancion(Archivo): #aqui aplico la herencia
  def __init__(self, titulo, artista, genero, peso_mb, duracion):
    super().__init__(titulo, duracion, peso_mb)
    self.artista = artista
    self.genero= genero 
    
  def __str__(self):
      return f"Titulo:{self.titulo} Artista:{self.artista} Duración:{self.duracion} Género:{self.genero}"

 