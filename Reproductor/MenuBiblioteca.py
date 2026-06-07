''' 
Created on March, 2026
@author: isaighernandez
'''
from Cancion import Cancion

class MenuBiblioteca:
    def __init__(self, encabezado, usuario):
        self.encabezado = encabezado
        self.usuario = usuario

    def desplegar_menu(self):
        print(f"\n=== {self.encabezado.upper()} ===")
        print("¿QUÉ DESEAS HACER?:")
        lista_opciones = [ "VER TODAS LAS CANCIONES ","AÑADIR CANCIÓN","REGRESAR AL MENÚ PRINCIPAL"]
        i=1
        for opcion in lista_opciones:
         print(i,opcion)
         i += 1
       
        while True:
         try:
            opciones = int(input("SELECCIONE UNA OPCIÓN: "))
            return opciones
         except ValueError:
                print("Debes ingresar un número válido.")

    def procesar_opciones(self):
        while True:
            opciones = self.desplegar_menu()
            
            if opciones == 1:
                self.usuario.mostrar_biblioteca()
                
            elif opciones == 2:
                print("\n=== AÑADIR NUEVA CANCIÓN ===")
                titulo = input("Título: ")
                artista = input("Artista: ")
                genero = input("Género: ")
                try:
                    peso = float(input("Peso en MB: "))
                    duracion = int(input("Duración: "))
                    nueva_cancion = Cancion(titulo, artista, genero, peso, duracion)
                    self.usuario.agregar_biblioteca(nueva_cancion)
                    print(f"¡'{titulo}' ha sido agregada exitosamente a tu biblioteca!")

                except ValueError:
                    print("Error: El peso o la duración deben ser números. Inténtalo de nuevo.")


            elif opciones == 3:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")