#Ejercicio1

lista_range = list(range(4, 101, 4))
print(lista_range)

#Ejercicio2

lista_indexingnegativo = ["Perro", "Gato", "Hámster", "Tortuga", "Pez"]
print(lista_indexingnegativo[-2])

#Ejercicio3

lista_vacia = []
print("Cree una lista con 3 elementos.")
for i in range(3):
    agregar_lista = input("Agregue el próximo elemento de la lista: ")
    lista_vacia.append(agregar_lista)
print(lista_vacia)

#Ejercicio4

animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[-3] = "loro"
animales[-1] = "oso"
print(animales)

#Ejercicio5

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#Lo que sucede es que el programa utiliza la función .remove() para eliminar
#un elemento, siendo el mayor elemento de la lista, esto indicado mediante la
#función max()

#Ejercicio6

lista_cinco = list(range(10, 31, 5))
print(lista_cinco[0], lista_cinco[1])

#Ejercicio7

autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1] = "porsche"
autos[2] = "renault"
print(autos)

#Ejercicio8

lista_dobles = []
lista_dobles.append(5 * 2)
lista_dobles.append(10 * 2)
lista_dobles.append(15 * 2)
print(lista_dobles)

#Ejercicio9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#EjercicioA

compras[2].append("jugo")

#EjercicioB

compras[1][1] = "tallarines"

#EjercicioC

compras[0].remove("pan")

#EjercicioD

print(compras)

#Ejercicio10

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]
print(lista_anidada)


