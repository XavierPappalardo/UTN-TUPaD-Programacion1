#Funciones

#Ejercicio 1

def repetirFactorial(numero_factorial):
    if numero_factorial == 1:
        print("El factorial del número '1' es igual a: 1")
    else:
        print(f"El factorial del número '{numero_factorial}' es igual a: {factorial(numero_factorial)}")
        return repetirFactorial(numero_factorial - 1)
        
        
def factorial(numero_factorial):
    if numero_factorial == 1:
        return 1
    else:
        return numero_factorial * (factorial(numero_factorial - 1))

#Ejercicio 2

def fibonacci(numero1, numero2):
    return numero1 + numero2

def repetirFibonacci(numero_secuencia):
    if numero_secuencia == 1:
        print(f"La secuencia Fibonacci del número elegido es: {secuencia}")
    else:
        numero1 = secuencia[-1]
        numero2 = secuencia[-2]
        agregar_secuencia = fibonacci(numero1, numero2)
        secuencia.append(agregar_secuencia)
        return repetirFibonacci(numero_secuencia - 1)

#Ejercicio 3

def potencia(numero_base, numero_exponente):
    if numero_exponente ==  0:
        return 1
    else:
        return numero_base * potencia(numero_base, numero_exponente - 1)

#Ejercicio 4

def exponente_de_dos(potencia_dos, numero_decimal):
    if numero_decimal > (2 ** (potencia_dos + 1)):
        return exponente_de_dos(potencia_dos + 1, numero_decimal)
    elif numero_decimal < (2 ** (potencia_dos + 1)):
        return potencia_dos
    elif numero_decimal == (2 ** (potencia_dos + 1)):
        potencia_dos += 1
        return potencia_dos

def convertir_binario(numero_decimal, exponente, binario):
    if exponente < 0:
        return binario
    if numero_decimal >= 2 ** exponente:
        binario.append("1")
        numero_decimal -= 2 ** exponente
        return convertir_binario(numero_decimal, exponente - 1, binario)
    else:
        binario.append("0")
        return convertir_binario(numero_decimal, exponente - 1, binario)
            
#Ejercicio 5

def verificar_palabra(palabra):
    numeros = "1234567890"
    tilde = "áéíóúÁÉÍÓÚ"
    espacio = " "
    abecedario = "abcdefghijklmnñopqrstuvxyz"
    for i in palabra:
        if i in tilde or i in espacio or i in numeros:
            return False
        else:
            continue
    return True
            
def es_palindromo(palabra, primer_letra, ultima_letra):
    if len(palabra) == 1:
        return True
    else:
        if primer_letra > ultima_letra:
            return True
        else:
            if palabra[primer_letra] == palabra[ultima_letra]:
                return es_palindromo(palabra, primer_letra + 1, ultima_letra - 1)
            else:
                return False

#Ejercicio 6

def suma_digitos(n, total, sumar_digito):
    if n - 10 > 0:
        sumar_digito = n % 10
        total += sumar_digito
        sumar_digito = 0
        return suma_digitos(n // 10, total, sumar_digito)
    else:
        sumar_digito = n
        total += sumar_digito
        return total

#Ejercicio 7

def contar_bloques(n, total_bloques):
    if n == 1:
        return total_bloques + 1
    else:
        total_bloques += n
        return contar_bloques(n - 1, total_bloques)

#Ejercicio 8

def contar_digito(numero, digito, cantidad_veces):
    if numero < 10:
        if numero == digito:
            return cantidad_veces + 1
        else:
            return cantidad_veces
    else:
        if numero % 10 == digito:
            cantidad_veces += 1
            return contar_digito(numero // 10, digito, cantidad_veces)
        else:
            return contar_digito(numero // 10, digito, cantidad_veces)
    
#Programa principal

#Ejercicio 1

while True:
    try:
        numero_factorial = int(input("Ingrese un número para calcular su factorial y el de sus números anteriores: "))
        repetirFactorial(numero_factorial)
        break
    except ValueError:
        print("Por favor, ingrese un número entero")

#Ejercicio 2

#Lista auxiliar para secuencia Fibonacci

secuencia = [0, 1, 1]

while True:
    try:
        numero_secuencia = int(input("Ingrese un número para realizar su secuencia Fibonacci: "))
        repetirFibonacci(numero_secuencia)
        break
    except ValueError:
        print("Por favor, ingrese un número entero")

#Ejercicio 3

while True:
    try:
        numero_base = int(input("Ingrese un número para que lo elevemos por un exponente: "))
        numero_exponente = int(input("Ahora ingrese el valor del exponente: "))
        print(f"El resultado de elevar el número '{numero_base}' por el exponente '{numero_exponente}' es de: {potencia(numero_base, numero_exponente)}")
        break
    except ValueError:
        print("La base y el exponente deben ser números enteros. Por favor, ingrese números enteros para ambos")

#Ejercicio 4

#Lista auxiliar para formar el número binario

binario = []

while True:
    try:
        numero_decimal = int(input("Ingrese un número decimal y lo convertiremos a su contraparte binaria: "))

        #Función auxiliar para buscar la mayor potencia de 2 menor a numero_decimal

        potencia_dos = 1
        exponente = exponente_de_dos(potencia_dos, numero_decimal)

        convertir_binario(numero_decimal, exponente, binario)
        print(f"El equivalente binario del número '{numero_decimal}' es: ", end="")
        for i in binario:
            print(i, end="")
        print("\n", end="")
        break
    except ValueError:
        print("Por favor, ingrese un número entero")

#Ejercicio 5

while True:
    try:
        palabra = input("Escriba una palabra y comprobaremos si es palíndroma o no: ")
        verificar = verificar_palabra(palabra)
        if verificar == False:
            print("Ingrese una palabra por favor. Ésta debe ser sin espacios ni tíldes")
            continue
        else:
            primer_letra = 0
            ultima_letra = len(palabra) - 1
            palindromo = es_palindromo(palabra, primer_letra, ultima_letra)
            print(f"La palabra ingresada es un palíndromo: {palindromo}")
            break
    except ValueError:
        print("Ingrese una palabra para poder verificar si es o no palíndroma")

#Ejercicio 6

while True:
    try:
        numero_digitos = int(input("Ingrese un número y le diremos la suma de todos los números de sus dígitos: "))
        total = 0
        sumar_digito = 0
        total = suma_digitos(numero_digitos, total, sumar_digito)
        print(f"La suma de los números de cada dígito del número ingresado es igual a: {total}")
        break
    except ValueError:
        print("Ingrese un número entero por favor")

#Ejercicio 7

while True:
    try:
        numero_bloques = int(input("Ingrese la cantidad de bloques de la base y le diremos la cantidad necesaria para construir toda la pirámide: "))
        if numero_bloques < 1:
            print("Debe ingresar un número positivo para poder realizar la pirámide")
            continue
        else:
            total_bloques = 0
            total_bloques = contar_bloques(numero_bloques, total_bloques)
            print(f"El total de bloques que componen la pirámide es: {total_bloques} bloques")
            break
    except ValueError:
        print("Ingrese un número entero por favor")

#Ejercicio 8

while True:
    try:
        numero = int(input("Ingrese un número: "))
        digito = int(input("Ingrese un dígito y veremos cuántas veces aparece en el número ingresado anteriormente: "))
        auxiliar_numero = numero
        cantidad_veces = 0
        cantidad_veces = contar_digito(numero, digito, cantidad_veces)
        print(f"El dígito ingresado aparece {cantidad_veces} veces en el número {auxiliar_numero}")
        break
    except ValueError:
        print("Ingrese un número entero por favor")
        
        
