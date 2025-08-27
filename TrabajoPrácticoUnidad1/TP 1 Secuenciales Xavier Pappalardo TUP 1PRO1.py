#Ejercicio 1

print("Hola Mundo!")

#Ejercicio 2

nombre = input("Ingrese su nombre por favor: ")
print(f"Hola {nombre}!")

#Ejercicio 3

nombre = input("Ingrese su nombre por favor: ")
apellido = input("Ahora ingrese su apellido: ")
edad = input("Ahora ingrese su edad: ")
lugar_residencia = input("Para terminar, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

#Ejercicio 4

radio = int(input("Ingrese por favor el radio de un círculo y calcularemos su perímetro y su área: "))
perimetro = 2 * 3.14 * radio
area = 3.14 * radio ** 2
print(f"El perímetro del círculo ingresado es de {perimetro}cm y su área es de {area}cm2")

#Ejercicio 5

segundos = int(input("Ingrese una cantidad de segundos y le diremos a cuántas horas equivale: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

#Ejercicio 6

tabla = int(input("Escriba por favor un número y le daremos la tabla de multiplicar de dicho número: "))
for i in range(10):
    print(f"{tabla} x {i + 1} = {tabla * (i + 1)}")

#Ejercicio 7

print("Escriba por favor 2 números enteros distintos de 0 y le mostraremos el resultado de las operaciones entre ellos")
entero = False

while entero == False:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ahora ingrese el segundo número: "))
    if num1 == 0 or num2 == 0:
        print("Por favor ingrese un número válido. Intente de nuevo")
    else:
        entero = True

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"El resultado de sumar ambos números es: {suma}\nEl resultado de restar el segundo número al primero es: {resta}\nEl resultado de multiplicar ambos números es: {multiplicacion}\nEl resultado de dividir el primer número por el segundo es: {division}")

#Ejercicio 8

print("Vamos a calcular su índice de masa corporal utilizando su altura y su peso")
peso = int(input("Ingrese por favor su peso en kilogramos: "))
altura = float(input("Ahora ingrese su altura en metros: "))
indice_masa_corporal = peso / (altura ** 2)
print(f"El IMC con los datos ingresados es de: {indice_masa_corporal}")

#Ejercicio 9

celsius = float(input("Ingrese una temperatura en grados Celsius y la convertiremos a grados Farenheit: "))
farenheit = celsius * 9/5 + 32
print(f"{celsius} grados Celsius es igual a {farenheit} grados Farenheit")

#Ejercicio 10

print("Ingrese 3 números y le daremos el promedio de dichos números")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3 ) / 3
print(f"El promedio de los 3 números ingresados es: {promedio}")
