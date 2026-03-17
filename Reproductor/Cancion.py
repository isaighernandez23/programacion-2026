''' 
Created on March, 2026
@author: isaighernandez

'''
class Cancion:

  def __init__(self, titulo, artista, duracion,genero):
    self.artista = artista
    self.titulo = titulo 
    self.duracion = duracion # duracion de la cancion
    self.genero = genero
    self.reproduciendo = False # ver si la canción esta en reproducción
    
  def __str__(self):
      return f"Titulo:{self.titulo} Artista:{self.artista} Duración:{self.duracion} Género:{self.genero}"

  def reproducir(self):
    self.reproduciendo = True
    return f"REPRODUCIENDO:{self.titulo}"

  def pausar(self):
   self.reproduciendo= False
   return "REPRODUCCION EN PAUSA"