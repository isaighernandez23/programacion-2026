class Archivo:
    def __init__(self, titulo,duracion, peso_mb):
        self.titulo = titulo # aqui estamos en un entorno en el que los archivos no tienen extension, asi que el titulo es igual al nombre del archivo 
        self.peso_mb = peso_mb                
        self.reproduciendo = False # ver si la canción esta en reproducción
        self.duracion= duracion
    def __str__(self):
        return f"[{self.titulo} | {self.peso_mb} MB]"
    
    def reproducir(self):
      self.reproduciendo = True
      return f"REPRODUCIENDO:{self.titulo}"
    def pausar(self):
      self.reproduciendo= False
      return "REPRODUCCION EN PAUSA"