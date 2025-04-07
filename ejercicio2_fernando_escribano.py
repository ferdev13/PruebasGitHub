#Ejercicio 2
#Fernando Escribano
#14/03/25

import os
os.system("cls") 

class Articulo:
    def __init__(self, identificadores, nombres, cantidades, descripciones, precios):

        self.identificadores = identificadores
        self.nombres = nombres
        self.cantidades = cantidades
        self.descripciones = descripciones
        self.precios = precios

    def __str__(self):
        return f"ID: {self.identificadores}, Nombre: {self.nombres}, Cantidades: {self.cantidades}, Descripcion: {self.descripciones}, Precio: {self.precios}"

class Tienda:
    def __init__(self):
        self.articulos = []
    
    def guardar_ariticulo(self):
        try:
            identificadores = int(input("Id: "))
            nombres = input("Nombre: ")
            cantidades = input("Cantidad: ")
            descripciones = input("Descripcion: ")
            precios = float(input("Precio: "))
            
            articulo = Articulo(identificadores, nombres, cantidades, descripciones, precios)

            self.articulos.append(articulo)
            
            print("="*30)
            print(f"Articulo '{nombres}' creado exitosamente.")
        except ValueError as e:
            print(f"ERROR: {e}. Introduce un valor correcto")

    def mostrar_articulos(self):
        if not self.articulos:
            print("="*30)
            print("La despensa está vacía.")
            return
        
        print("="*30)
        print("DETALLE DE LOS ARTICULOS")
        print("="*30)

        for articulo in self.articulos:
            print(f"Id: {articulo.identificadores}")
            print(f"Nombre: {articulo.nombres}")
            print(f"Cantidades: {articulo.cantidades}")
            print(f"Descripción: {articulo.descripciones}")
            print(f"Precio: {articulo.precios}")
            print("="*30)
        
    def borrar_articulo(self):
        if not self.articulos: 
            print("=" * 30)
            print("La despensa está vacía.")
            return

        self.mostrar_articulos()  

        articulo_eliminar = input("Escribe el nombre del articulo a eliminar: ")
        
        for articulo in self.articulos:
            if articulo.nombres == articulo_eliminar:
                self.articulos.remove(articulo) 
                print("=" * 30)
                print(f"Articulo '{articulo_eliminar}' borrado.")
                return 

        self.mostrar_articulos() 

def muestra_menu():
            print("="*30)
            print("1.Añadir articulo")
            print("2.Mostrar articulo")
            print("3.Borrar articulo")
            print("4.Salir")

def salir_programa():
            print("="*30)
            print("Saliendo del programa...")
            print("="*30)        

def menu():
    ejecutando = True
    tienda = Tienda()

    while ejecutando:
        muestra_menu()
        try:
            opcion=int(input("Introduzca una opción: "))

            if opcion==1:
                tienda.guardar_ariticulo()
            elif opcion==2:
                tienda.mostrar_articulos()
            elif opcion==3:
                tienda.borrar_articulo()
            elif opcion==4:
                salir_programa()
                ejecutando = False
            else:
                print("Introduzca una opción válida!")
        except ValueError:
            print("Introduzca una opción válida!")
        
if __name__ == "__main__":
    menu()