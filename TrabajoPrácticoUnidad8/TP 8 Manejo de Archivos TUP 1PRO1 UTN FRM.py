#Ejercicio2

#Lista con diccionarios de productos

productos = []

diccionario = {}

#Verifica si existe el archivo y lee los productos

import os

def modificarLinea():
    global productos
    if os.path.exists("productos.txt") == True:
        with open("productos.txt", "r") as archivo:
            archivo.readline()
            for linea in range(3):
                linea_modificada = archivo.readline().split(",")
                dato_producto = (linea_modificada[0].strip())
                dato_precio = (linea_modificada[1].strip())
                dato_cantidad = (linea_modificada[2].strip())
                print(f"Producto: {dato_producto} | Precio: {dato_precio} | Cantidad: {dato_cantidad}")
                diccionario = {
                    "nombre": dato_producto,
                    "precio": dato_precio,
                    "cantidad": dato_cantidad,
                    }
                productos.append(diccionario)
    else:
        print("El archivo no existe. Si lo desea, cree uno a continuación")
    return

#Ejercicio3

#Agregar productos

def agregarProductos():
    global productos
    continuar = True
    while continuar == True:
        agregar_producto = input("Si desea agregar nuevos productos a la lista anterior, ingrese 'a', en caso contrario, ingrese 'b': ")
        if agregar_producto.lower() == "a":
            try:
                nuevo_producto = input("Ingrese un nuevo producto: ")
                nuevo_precio = float(input("Ingrese el precio del nuevo producto: "))
                nuevo_cantidad = int(input("Ingrese la cantidad de existencias del nuevo producto: "))

                #Ejercicio4

                diccionario_agregar = {
                    "nombre": nuevo_producto.lower(),
                    "precio":  nuevo_precio,
                    "cantidad": nuevo_cantidad,
                    }
                productos.append(diccionario_agregar)


            except ValueError:
                print("Dato inválido. Ingrese por favor un tipo de dato válido")
        elif agregar_producto.lower() == "b":
            print("No se agregarán más productos")
            return productos
        else:
            print("Dato inválido, intente de nuevo")

#Ejercicio5

#Buscar producto

def buscarProducto():
    continuar_buscando = True
    while continuar_buscando == True:
        validacion_buscar = input("Si desea buscar un producto, ingrese 'a', en caso contrario, ingrese 'b': ")
        if validacion_buscar.lower() == "a":
            producto_buscar = input("Ingrese el nombre del producto que desea buscar: ")
            for i in productos:
                if i["nombre"].lower() == producto_buscar.lower():
                    print(f'Producto: {i["nombre"]} | Precio: {i["precio"]} | Cantidad: {i["cantidad"]}')
        elif validacion_buscar.lower() == "b":
            print("No se seguirán buscando productos")
            return
        else:
            print("Dato inválido, por favor intente de nuevo")

#Ejercicio6

def reescribirArchivo():
    with open("productos.txt", "w") as archivo:
        archivo.write("nombre, precio, cantidad\n")
        for i in productos:
            archivo.write(f"{i["nombre"]}, ")
            archivo.write(f"{i["precio"]}, ")
            archivo.write(f"{i["cantidad"]}\n")
    return

#Llamado de las funciones
        
modificarLinea()

agregarProductos()
        
buscarProducto()

reescribirArchivo()
