''' 
Created on March, 2026
@author: isaighernandez23

'''
class Cancion:
  def __init__(self, titulo, artista, duracion, genero):
    self.artista = artista
    self.duracion = duracion # duracion de la cancion
    self.genero = genero
    self.reproduciendo = False # ver si la canción esta en reproducción
    self.titulo = titulo 

  def informacion_cancion(self):
    print(" Información de la Canción")
    print(f"Título: {self.titulo}")
    print(f"Artista: {self.artista}")
    print(f"Duración: {self.duracion} segundos") # duracion en segundos
    print(f"Género: {self.genero}")
    
  def reproducir(self):
    self.reproduciendo = True
    print("REPRODUCIENDO:", self.titulo )

  def pausar(self):
    self.reproduciendo= False

    print("REPRODUCCION EN PAUSA")

