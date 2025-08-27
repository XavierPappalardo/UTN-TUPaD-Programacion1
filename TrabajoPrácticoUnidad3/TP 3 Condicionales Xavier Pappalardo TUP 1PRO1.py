#Ejercicio1

mayor_edad = int(input("Ingrese su edad y verificaremos si es mayor de edad: "))
if mayor_edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#Ejercicio2

nota_aprobado = int(input("Ingrese su nota para saber si está aprobado o desaprobado: "))
if nota_aprobado > 6 and nota_aprobado > 0 and nota_aprobado < 11:
    print("Aprobado")
elif nota_aprobado < 6 and nota_aprobado > 0 and nota_aprobado < 11:
    print("Desaprobado")
else:
    print("Nota inválida, por favor intente de nuevo")

#Ejercicio3

numero_par = int(input("Ingrese un número par: "))
if numero_par % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio4

edad_usuario = int(input("Por favor, ingrese su edad y le informaremos a cual grupo etario pertenece: "))
if edad_usuario < 12 and edad_usuario >= 0:
    print("Usted es un/a niño/a")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Usted es un/a adolescente")
elif edad_usuario >= 18 and edad_usuario < 30:
    print("Usted es un/a adulto/a joven")
elif edad_usuario >= 30:
    print("Usted es un/a adulto/a")
else:
    print("Ingrese una edad válida")
    
#Ejercicio5

longitud_contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if len(longitud_contraseña) >= 8 and len(longitud_contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio6

from statistics import mode, median, mean
import random 
lista_numeros = [random.randint(1, 100) for i in range(50)]
media = mean(lista_numeros)
moda = mode(lista_numeros)
mediana = median(lista_numeros)
print(f"De la lista de números generada aleatoriamente, la media es {media}, la moda es {moda} y la mediana es {mediana}")

#Ejercicio7

frase = input("Ingrese una frase o palabra por favor: ")
longitud_frase = frase[-1]
if longitud_frase in "aeiou":
    print(f"{frase}!")
else:
    print(frase)

#Ejercicio8
    
nombre = input("Ingrese su nombre por favor: ")
print("Ahora diga si quiere su nombre escrito totalmente en mayúscula, totalmente en minúscula o con sólo la primer letra mayúscula.")
mayuscula_minuscula = int(input("En caso de que desee la primera opción, escriba 1, en caso de querer la segunda, escriba 2, y si desea la tercera opción, ingrese el número 3: "))
if mayuscula_minuscula == 1:
    print(nombre.upper())
elif mayuscula_minuscula == 2:
    print(nombre.lower())
elif mayuscula_minuscula == 3:
    print(nombre.title())
else:
    print("Ingrese un número válido por favor")


#Ejercicio9

magnitud_terremoto = int(input("Ingrese la magnitud de un terremoto y le diremos su magnitud: "))
if magnitud_terremoto < 3:
    print("Muy leve(Imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve(Ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado(Sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte(Puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy fuerte(Puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Externo(Puede causar graves daños a gran escala)")

#Ejercicio10
    
print("Vamos a calcular en qué estación estamos.")
hemisferio = input("Para empezar, indique en que hemisferio está ubicado, si en el norte o el sur: ")
mes = input("Ahora indique en que mes estamos: ")
dia = int(input("Ahora, para finalizar, indique el día de la fecha: "))
if hemisferio.lower() == "norte":
    if (mes.lower() == "enero") or (mes.lower() == "febrero") or (mes.lower() == "diciembre" and dia >= 21) or (mes.lower() == "marzo" and dia <= 20):
        print("Estamos en invierno")
    elif (mes.lower() == "abril") or (mes.lower() == "mayo") or (mes.lower() == "marzo" and dia >= 21) or (mes.lower() == "junio" and dia <= 20):
        print("Estamos en primavera")
    elif (mes.lower() == "julio") or (mes.lower() == "agosto") or (mes.lower() == "junio" and dia >= 21) or (mes.lower() == "septiembre" and dia <= 20):
        print("Estamos en verano")
    elif (mes.lower() == "octubre") or (mes.lower() == "noviembre") or (mes.lower() == "septiembre" and dia >= 21) or (mes.lower() == "diciembre" and dia <= 20):
        print("Estamos en otoño")
elif hemisferio.lower() == "sur":
    if (mes.lower() == "enero") or (mes.lower() == "febrero") or (mes.lower() == "diciembre" and dia >= 21) or (mes.lower() == "marzo" and dia <= 20):
        print("Estamos en verano")
    elif (mes.lower() == "abril") or (mes.lower() == "mayo") or (mes.lower() == "marzo" and dia >= 21) or (mes.lower() == "junio" and dia <= 20):
        print("Estamos en otoño")
    elif (mes.lower() == "julio") or (mes.lower() == "agosto") or (mes.lower() == "junio" and dia >= 21) or (mes.lower() == "septiembre" and dia <= 20):
        print("Estamos en invierno")
    elif (mes.lower() == "octubre") or (mes.lower() == "noviembre") or (mes.lower() == "septiembre" and dia >= 21) or (mes.lower() == "diciembre" and dia <= 20):
        print("Estamos en primavera")
else:
    print("Los datos ingresados son inválidos, intente de nuevo")

