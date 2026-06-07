''' 
Created on March, 2026
@author: isaighernandez

'''
import csv
from Cancion import *
from MenuP import *
from Playlist import *
from Usuario import Usuario
class Main:
  pass

usuario1= Usuario("isaighernandez23","isaighernandez23","asdfghhj")
playlist1=Playlist("Rolas")
nombre_archivo = "Rolas.csv"

try: #moduo archivos csv 
    with open(nombre_archivo, mode='r') as archivo:
        lector = csv.reader(archivo)
        
        next(lector)
        for fila in lector:
            if len(fila) >= 5:
                titulo = fila[0].strip()
                artista = fila[1].strip()
                genero = fila[2].strip()
                peso = float(fila[3])
                duracion = int(fila[4])
            
                nueva_cancion = Cancion(titulo, artista, genero, peso, duracion)
                
                usuario1.agregar_biblioteca(nueva_cancion)
                playlist1.añadir_cancion(nueva_cancion)
                
    print("Las canciones se han cargado automáticamente")

except FileNotFoundError:
    print(f" No se encontró el archivo '{nombre_archivo}")
except Exception :
    print(f"Ocurrió un error al procesar el archivo")


menu = MenuP("=== BIENVENIDO A TU REPRODUCTOR MUSICAL ===",)

menu.dar_bienvenida()
while True:
  eleccion = menu.desplegar_menu()

  menu.procesar_opciones(eleccion,playlist1,usuario1)
  if eleccion == 3:
    break


