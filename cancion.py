#@ author : isai
class cancion:
  def __init__(self, titulo, artista, duracion, genero):
    self.artista = artista
    self.duracion = duracion # duracion de la cancion
    self.genero = genero
    self.reproduciendo= False # ver si la canción esta en reproducción

  def informacion_cancion(self):
    print(" Información de la Canción")
    print(f"Título: {self.titulo}")
    print(f"Artista: {self.artista}")
    print(f"Duración: {self.duracion} segundos") # duracion en segundos
    print(f"Género: {self.genero}")
