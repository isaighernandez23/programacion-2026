class MenuCancion:
    def __init__(self, encabezado, cancion):
        self.encabezado = encabezado
        self.cancion = cancion

    def desplegar_menu(self):
        print(f"\n=== {self.encabezado.upper()} ===")
        print(f"Canción: {self.cancion.titulo}")
        lista_opciones = ["Reproducir","Pausar","Informacion de la cancion","Regresar al menú principal"]
        
        for opcion in lista_opciones:
          print(i,opcion)
          i += 1
            
        while True:
            try:
                eleccion = int(input("SELECCIONE UNA OPCIÓN: "))
                return eleccion
            except ValueError:
                print("Debes ingresar un número.")

    def procesar_opciones(self):
        while True:
            eleccion = self.desplegar_menu()
            if eleccion == 1:
                print(self.cancion.reproducir())

            elif eleccion == 2:
                print(self.cancion.pausar())

            elif eleccion == 3:
                print(self.cancion) 

            elif eleccion == 4:
                print("Regresando al menú principal...")
                break
            
            else:
                print("Opción no válida.")