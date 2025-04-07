#Ejercicio 3
#Fernando Escribano
#14/03/25

import os
import mysql.connector
os.system("cls")

def conectar_bd():
    """Conecta con la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="EXAMEN"
        )
        if conexion.is_connected():
            print("Conectado a la base de datos!!") 
            return conexion
    
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None
    
QUERY_INSERT_ARTICULO = "INSERT INTO articulos (nombre, cantidad, descripcion, precio) VALUES ( %s, %s, %s, %s)"
QUERY_UPDATE_STOCK = "UPDATE articulos SET cantidad = cantidad - %s WHERE id = %s"
QUERY_SELECT_STOCK = "SELECT cantidad FROM articulos WHERE id = %s"
QUERY_SELECT_ARTICULOS = "SELECT * FROM articulos"

    
def guardar_ariticulo(conexion):
    
    nombre = input("Nombre: ")
    cantidad = input("Cantidad: ")
    descripcion = input("Descripcion: ")
    precio = float(input("Precio: "))

    try:
        cursor = conexion.cursor()
        cursor.execute(QUERY_INSERT_ARTICULO, (nombre, cantidad, descripcion, precio))
        conexion.commit()
        print("Nuevo artículo guardado!")
    except mysql.connector.Error as error:
        print("Error al guardar el artículo: ", error)
    except Exception as error:  
        print("Ocurrió un error inesperado:", error)
    finally:
        if cursor:
            cursor.close()   

def listar_articulos_completa(conexion):
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute(QUERY_SELECT_ARTICULOS)
        print("\nLista de artículos disponibles:")
        
        for articulos in cursor:
            print(f"ID: {articulos[0]}, Nombre: {articulos[1]}, Cantidad: {articulos[2]}, Descripcion: {articulos[3]}, Precio: {articulos[4]}")
    except mysql.connector.Error as error:
        print("Error al listar los artículos: ", error)
    except Exception as error:  
        print("Ocurrió un error inesperado:", error)
    finally:
        if cursor:
            cursor.close()

def borrar_articulo(conexion):
    listar_articulos_completa(conexion) 
    id_articulo = int(input("Ingrese el ID del artículo: "))
    cantidad = int(input("Ingrese la cantidad vendida: "))
    cursor = None

    try:
        cursor = conexion.cursor()
        cursor.execute(QUERY_SELECT_STOCK, (id_articulo,))
        resultado = cursor.fetchone()
        
        if resultado is None:
            print("El artículo no existe.")
            return
        
        stock_actual = resultado[0]
        
        if cantidad <= 0:
            print("La cantidad vendida debe ser mayor que cero.")
        elif cantidad > stock_actual:
            print("No hay suficiente stock disponible.")
        else:
            cursor.execute(QUERY_UPDATE_STOCK, (cantidad, id_articulo))
            conexion.commit()
            print("Venta registrada con éxito.")

    except mysql.connector.Error as error:
        print("Error al registrar la venta: ", error)
    except Exception as error:  
        print("Ocurrió un error inesperado:", error)
    finally:
        if cursor:
            cursor.close()

def muestra_menu():
    print("\nMenú:")
    print("1. Ingresar artículo")
    print("2. Vender artículo")
    print("3. Ver lista de artículos")
    print("4. Salir")

def salir_programa(conexion):
    print("="*30)
    print("Saliendo del programa...")
    print("="*30)
    conexion.close()

def menu():
    ejecutando = True
    conexion = conectar_bd()

    if conexion is None:
        print("No se pudo conectar a la base de datos. Saliendo...")
        return

    while ejecutando:
        muestra_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                guardar_ariticulo(conexion)
            elif opcion == 2:
                borrar_articulo(conexion)
            elif opcion == 3:
                listar_articulos_completa(conexion)
                print("Fallo en la sentecia sql")
            elif opcion == 4:
                salir_programa(conexion)
                ejecutando = False
            else:
                print("Opción no válida, intente nuevamente.")
        except ValueError:
            print("Introduzca una opción válida!")
        except mysql.connector.Error as e:
            print("Error en la base de datos: ", e)

if __name__ == "__main__":
    menu()