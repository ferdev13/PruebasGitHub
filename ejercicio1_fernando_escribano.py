#Ejercicio 1
#Fernando Escribano
#14/03/25

import os
os.system("cls") 

identificadores = []
nombres = []
cantidades = []
descripciones = []
precios = []

def guardar_ariticulo(identificadores, nombres, cantidades, descripciones, precios):
    while True:
        identificador = int(input("Id: "))
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        descripcion = input("Descripcion: ")
        precio = float(input("Precio: "))
        break

    identificadores.append(identificador)
    nombres.append(nombre)
    cantidades.append(cantidad)
    descripciones.append(descripcion)
    precios.append(precio)

    return identificadores, nombres, cantidades, descripciones, precios

def mostrar_articulos(identificadores, nombres, cantidades, descripciones, precios):

    if len(identificadores) > 0:
        print("\nArticulos:")
        for i in range(len(identificadores)):
            print(f"{i+1} ID: {identificadores[i]}, Nombre: {nombres[i]}, Precio: {cantidades[i]}, Cantidad: {descripciones[i]}, Precio: {precios[i]}")

    else:
        print("="*30)
        print("La lista de artículos está vacía")

def borrar_articulo(identificadores):
    if not identificadores: 
        print("=" * 30)
        print("La despensa está vacía.")
        return

    mostrar_articulos(identificadores, nombres, cantidades, descripciones, precios)  

    articulo_eliminar = int(input("Escribe el id del articulo a eliminar: "))
    identificadores.remove(articulo_eliminar)

    mostrar_articulos(identificadores, nombres, cantidades, descripciones, precios) 

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

    while ejecutando:
        muestra_menu()
        try:
            opcion=int(input("Introduzca una opción: "))

            if opcion==1:
                guardar_ariticulo(identificadores, nombres, cantidades, descripciones, precios)
            elif opcion==2:
                mostrar_articulos(identificadores, nombres, cantidades, descripciones, precios)
            elif opcion==3:
                borrar_articulo(identificadores)
            elif opcion==4:
                salir_programa()
                ejecutando = False
            else:
                print("Introduzca una opción válida!")
        except ValueError:
            print("Introduzca una opción válida!")
        
if __name__ == "__main__":
    menu()


print("="*30)