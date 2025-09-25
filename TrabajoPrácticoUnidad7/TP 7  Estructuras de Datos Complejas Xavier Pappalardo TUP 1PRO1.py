#Ejercicio1

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

lista_frutas = list(precios_frutas.keys())

#Ejercicio3

print("\nDiccionario actualizado:")
print(precios_frutas)
print("\nLista de frutas:")
print(lista_frutas)

#Ejercicio4

contactos = {}

print("Carga de contactos:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto #{i + 1}: ")
    numero = input(f"Ingresá el número de teléfono de {nombre}: ")
    contactos[nombre] = numero

print("\n Consulta de contacto:")
consulta = input("Ingresá el nombre que querés buscar: ")

if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró ningún contacto con el nombre '{consulta}'")

#Ejercicio5

frase = input("\nIngresá una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("\nPalabras únicas:")
print(palabras_unicas)

print("\nRecuento de palabras:")
print(recuento)

#Ejercicio6

alumnos = {}

print("\nIngresá los datos de 3 alumnos:")
for i in range(3):
    nombre = input(f"Nombre del alumno #{i + 1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota #{j + 1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")

#Ejercicio7

parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107}

ambos = parcial1 & parcial2

solo_uno = parcial1 ^ parcial2

al_menos_uno = parcial1 | parcial2

print("\nAprobados en ambos parciales:", ambos)
print("Aprobados solo en uno de los dos:", solo_uno)
print("Aprobados en al menos uno:", al_menos_uno)

#Ejercicio8

stock_productos = {
    "Arroz": 20,
    "Fideos": 35,
    "Aceite": 15
}

print("Gestión de stock de productos")
print("Opciones:")
print("1 - Consultar stock")
print("2 - Agregar unidades a producto existente")
print("3 - Agregar nuevo producto")

opcion = input("\nSeleccioná una opción (1, 2 o 3): ")

if opcion == "1":
    producto = input("Ingresá el nombre del producto a consultar: ")
    if producto.capitalize() in stock_productos:
        producto = producto.capitalize()
        print(f"Stock de {producto}: {stock_productos[producto]} unidades")
    else:
        print(f"El producto '{producto}' no está en el inventario.")

elif opcion == "2":
    producto = input("Ingresá el nombre del producto: ")
    if producto in stock_productos:
        unidades = int(input(f"¿Cuántas unidades querés agregar a {producto}? "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
    else:
        print(f"El producto '{producto}' no existe. Usá la opción 3 para agregarlo.")

elif opcion == "3":
    producto = input("Ingresá el nombre del nuevo producto: ")
    unidades = int(input(f"Ingresá la cantidad inicial de unidades para {producto}: "))
    stock_productos[producto] = unidades
    print(f"Producto '{producto}' agregado con {unidades} unidades.")

else:
    print("Opción no válida. Por favor, elegí 1, 2 o 3.")

print("\nInventario actualizado:")
for producto, cantidad in stock_productos.items():
    print(f"{producto}: {cantidad} unidades")

#Ejercicio9

agenda = {}

print("Carga de eventos en la agenda:")
for i in range(3):
    dia = input(f"\nIngresá el día del evento #{i+1}: ").lower()
    hora = input(f"Ingresá la hora del evento #{i+1} (formato HH:MM): ")
    evento = input(f"¿Qué evento ocurre el {dia} a las {hora}? ")
    agenda[(dia, hora)] = evento

print("\nAgenda registrada:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia.capitalize()} a las {hora}: {evento}")

#Ejercicio10

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("\nDiccionario original:")
print(original)

print("\nDiccionario invertido:")
print(invertido)




