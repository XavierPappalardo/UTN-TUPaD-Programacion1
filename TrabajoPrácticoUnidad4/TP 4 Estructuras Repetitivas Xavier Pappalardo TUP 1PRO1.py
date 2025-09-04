#Ejercicio1

for i in range(101):
    print(i)

#Ejercicio2

numero_ejerciciodigitos = int(input("Ingrese un número y le diremos la cantidad de dígitos que posee: "))
cantidad_digitos = 0
numero_resta = 10
while numero_ejerciciodigitos > 0:
    numero_ejerciciodigitos -= numero_resta
    numero_resta *= 10
    cantidad_digitos += 1
print(f"La cantidad de dígitos del número ingresado es de {cantidad_digitos} dígito/s")

#Ejercicio3

print("Este programa suma todos los números entre los 2 números ingresados, excluyendo estos mismos.")
valor1 = int(input("Ingrese el primer número: "))
valor2 = int(input("Ingrese el segundo número: "))
inicio = min(valor1, valor2) + 1
fin = max(valor1, valor2)
suma_total = 0
for i in range(inicio, fin):
    suma_total += i
print(f"La suma de los números entre {valor1} y {valor2} es: {suma_total}")

#Ejercicio4

print("Ingrese números enteros y se sumarán en secuencia. Cuando quiera parar y ver el total acumulado, ingrese 0.")
numero_ingresado = int(input("Ingrese el primer número: "))
total_acumulado = numero_ingresado
while numero_ingresado != 0:
    numero_ingresado = int(input("Ingrese el próximo número: "))
    total_acumulado += numero_ingresado
print(f"El total acumulado de todos los números sumados es {total_acumulado}")

#Ejercicio5

import random
numero_aleatorio = random.randint(0,9)
intento = int(input("Ingrese un número y vea si adivinó el número aleatorio: "))
numero_intentos = 1
while intento != numero_aleatorio:
    intento = int(input("¡Incorrecto!Ingrese otro número: "))
    numero_intentos += 1
print(f"¡Correcto! Le tomó {numero_intentos} intento/s adivinar el número")

#Ejercicio6

for i in range(100, -1, -2):
    print(i)

#Ejercicio7

numero_suma = int(input("Ingrese un número y se sumarán todos los números entre 0 y el número ingresado: "))
total_suma = 0
for i in range(numero_suma):
    total_suma += i
print(f"El total acumulado entre 0 y el número ingresado es: {total_suma}")

#Ejercicio8

print("Ingrese 100 números y le diremos cuántos fueron pares, impares, positivos y negativos.")
total_positivos = 0
total_negativos = 0
total_pares = 0
total_impares = 0
for i in range(100):
    numero_ingresado = int(input("Ingrese el próximo número: "))
    if numero_ingresado % 2 == 0:
        total_pares += 1
        if numero_ingresado > 0:
            total_positivos += 1
        else:
            total_negativos += 1
    else:
        total_impares += 1
        if numero_ingresado > 0:
            total_positivos += 1
        else:
            total_negativos += 1
print(f"El total de números positivos, negativos, pares e impares respectivamente es de {total_positivos}, {total_negativos}, {total_pares} y {total_impares}.")

#Ejercicio9

total_sumado = 0
for i in range(100):
    numero_ingresado = int(input("Ingrese el próximo número: "))
    total_sumado += numero_ingresado
media = total_sumado / 100
print(f"La media de los números ingresados es de {media}")

#Ejercicio10

numero = input("Ingrese un número entero e invertiremos el orden de sus dígitos: ")
numero_invertido = ""
for i in range(len(numero) - 1, -1, -1):
    numero_invertido += numero[i]
print("El número ingresado invertido es: ", numero_invertido)
