''' 
Created on March, 2026
@author: isaighernandez

'''
from Cancion import * 
from Playlist import *
from MenuBiblioteca import MenuBiblioteca
from MenuPlaylist import MenuPlaylist

class MenuP:
  def __init__(self, encabezado):
    self.encabezado = encabezado

  def dar_bienvenida(self):
    print(self.encabezado.upper())


  def desplegar_menu(self):
    print("¿QUÉ DESEAS HACER?:")
    lista_opciones= ["ENTRAR A LA BIBLIOTECA","REPRODUCIR PLAYLIST","SALIR"]
    i = 1
    for opcion in lista_opciones:
     print(i,opcion)
     i += 1
    while True: 
     try:
      opciones = int(input("SELECCIONE UNA OPCIÓN: "))
      return opciones 
     except ValueError: # manejo de errores 
       print("Debes ingresar un número") 

  def procesar_opciones(self, opciones, playlist, usuario):
    if opciones == 1:
      print("ENTRANDO A LA BIBLIOTECA...")
      menu_biblio = MenuBiblioteca("Menú de Biblioteca", usuario)
      menu_biblio.procesar_opciones()

    elif opciones == 2:
      menu_pl = MenuPlaylist("Menú de Playlist", playlist)
      menu_pl.procesar_opciones()
      
      

    elif opciones == 3:
      print("SALIENDO DEL REPRODUCTOR. ¡VUELVA PRONTO!")

    else: 
      print("Opcion no valida")