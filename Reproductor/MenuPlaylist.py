''' 
Created on June, 2026
@author: isaighernandez

'''
class MenuPlaylist:
    def __init__(self, encabezado, playlist):
        self.encabezado = encabezado
        self.playlist = playlist

    def desplegar_menu(self):
        print(f"\n=== {self.encabezado.upper()} ===")
        print(f"PLAYLIST : {self.playlist.nombre_playlist}")
        lista_opciones = [ "Ver canciones en la playlist","Añadir canción a la playlist","Buscar cancion", "Reproducir playlist", "Regresar al menú principal"]
        i=1
        for opcion in lista_opciones:
         print(i,opcion)
         i += 1
            
        while True:
            try:
                seleccion = int(input("SELECCIONE UNA OPCIÓN: "))
                return seleccion
            except ValueError:
                print("Debes ingresar un número.")

    def procesar_opciones(self):
        while True:
            seleccion = self.desplegar_menu()
            if seleccion == 1:
                self.playlist.__str__() 

            elif seleccion == 2:
                titulo = input("Ingresa el título de la canción que deseas añadir: ")
                self.playlist.añadir_cancion(titulo)
                
            elif seleccion== 3:
                buscar=input("Ingresa el titulo de la cancion:")
                self.playlist.buscador(buscar)
                
            elif seleccion == 4:
                print(self.playlist.reproducir())

            elif seleccion == 5:
                print("Regresando al menú principal...")
                
                break

            else:
                print("Opción no válida.")