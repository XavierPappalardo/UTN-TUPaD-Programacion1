#Ejercicio1

#FunciónEjercicio1

def imprimir_hola_mundo():
    print("Hola Mundo!")

#ProgramaPrincipalEjercicio1
    
imprimir_hola_mundo()

#Ejercicio2

#FunciónEjercicio2

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#ProgramaPrincipalEjercicio2

nombre = input("Ingrese un nombre y recibirá un saludo personalizado: ")
saludar_usuario(nombre)

#Ejercicio3

#FunciónEjercicio3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#ProgramaPrincipalEjercicio3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio4

#FunciónEjercicio4 CalcularÁrea

def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return area

#FunciónEjercicio4 CalcularPerímetro

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

#ProgramaPrincipalEjercicio4

radio = int(input("Ingrese el radio de un círculo y le calcularemos el área y el perímetro: "))
print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))

#Ejercicio5

#FunciónEjercicio5

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

#ProgramaPrincipalEjercicio5

segundos = int(input("Ingrese una cantidad de segundos y le diremos cuántas horas son: "))
print(f"{segundos} segundo/s son iguales a {segundos_a_horas(segundos)} hora/s")

#Ejercicio6

#FunciónEjercicio6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        multiplo = i * numero
        print(f"{numero} x {i} = {multiplo}")

#ProgramaPrincipalEjercicio6

numero = int(input("Ingrese un número y le mostraremos su tabla de multiplicar del 1 al 10: "))
tabla_multiplicar(numero)

#Ejercicio7

#FunciónEjercicio7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    tupla = (suma, resta, multiplicacion, division)
    return tupla

#ProgramaPrincipalEjercicio7

print("Ingrese 2 números y los sumaremos, restaremos, multiplicaremos y dividiremos entre sí")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
print(f"Los resultados de sumar, restar, multiplicar y dividir los números son: {operaciones_basicas(numero1, numero2)}")

#Ejercicio8

#FunciónEjercicio8

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

#ProgramaPrincipalEjercicio8

print("Ingrese su peso y altura y calcularemos su Índice de Masa Corporal")
peso = float(input("Ingrese primero su peso: "))
altura = float(input("Ingrese ahora su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura)}")

#Ejercicio9

#FunciónEjercicio9

def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

#ProgramaPrincipalEjercicio9

celsius = float(input("Ingrese una temperatura en grados Celsius y le diremos su equivalente en grados Fahrenheit: "))
print(f"{celsius} grados Celsius es igual a {celsius_a_fahrenheit(celsius)} grados Fahrenheit")

#Ejercicio10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

#FunciónEjercicio10

print("Ingrese 3 notas y le diremos el promedio de las mismas")
nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))
print(f"El promedio de las notas ingresadas es: {calcular_promedio(nota1, nota2, nota3)}")
