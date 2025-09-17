#PrácticaIntegradora1

#ListaGolosinas

golosinas = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ["KitKat", "Chicles", "Caramelos de Menta", "Huevo Kinder", "Chetoos", "Twix", "M&M´s", "Papas Lays", "Milkybar", "Alfajor Tofi", "Lata Coca", "Chitos"], [20, 50, 50, 10, 10, 10, 10, 2, 10, 15, 20, 10]]

#DiccionarioEmpleados

empleados = {
    "1100" : "José Alonso",
    "1200" : "Federico Pacheco",
    "1300" : "Nelson Pereira",
    "1400" : "Osvaldo Tejada",
    "1500" : "Gastón García"
    }

#TuplaClaves

clavesTecnico = ("admin", "CCCDDD", "2020")

#GolosinasPedidas

golosinasPedidas = [[], [], []]

#PedirGolosina

def pedirGolosina():
    verificarLegajo = input("Ingrese su legajo para verificar que sea empleado de la empresa: ")
    legajoVerificado = False
    continuarPidiendo = True
    if verificarLegajo in empleados:
        legajoVerificado = True
    if legajoVerificado == True:
        while continuarPidiendo == True:
            pedido = input("Ingrese el código de la golosina que desee pedir. Recuerde que si desea no pedir más golosinas, ingrese 'No pedir más': ")
            if pedido.lower() == "no pedir más":
                return
            else:
                pedido = int(pedido)
                if pedido > 0 and pedido < 13:
                        cantidad = int(input("¿Cuántos desea pedir?: "))
                        if cantidad > 0:
                            if golosinas[2][pedido - 1] > 0 and golosinas[2][pedido - 1] > cantidad:
                                golosinas[2][pedido - 1] -= cantidad
                                print(f"Usted ha pedido {cantidad} {golosinas[1][pedido - 1]}")
                                if golosinas[1][pedido - 1] in golosinasPedidas[1]:
                                    for i in range(len(golosinasPedidas[0])):
                                        if golosinas[1][pedido - 1] == golosinasPedidas[1][i]:
                                            golosinasPedidas[2][i] += cantidad
                                else:
                                    golosinasPedidas[2].append(cantidad)
                                    golosinasPedidas[1].append(golosinas[1][pedido - 1])
                                    golosinasPedidas[0].append(golosinas[0][pedido - 1])
                            else:
                                print(f"Lo sentimos la golosina {golosinas[1][pedido - 1]} no se encuentra disponible, seleccione otra golosina o ingresa 'No pedir más' si no desea otra golosina.")
                else:
                    print("Por favor, ingrese un código de golosina válido.")
    else:
        print("Usted no es un empleado de la empresa")
        return
        
#MostrarGolosinas

def mostrarGolosinasDisponibles():
    print("La cantidad disponible de cada golosina es: ")
    for i in range(0, 12):
        print(f"{golosinas[1][i]}: {golosinas[2][i]}")
    return
    
#RellenarGolosinas

def rellenarMaquinaGolosinas():
    print("Antes de poder ejecutar la operación, ingrese las claves necesarias.")
    claves_correctas1 = input("Ingrese la primer clave: ")
    claves_correctas2 = input("Ingrese la segunda clave: ")
    claves_correctas3 = input("Ingrese la tercer clave: ")
    if claves_correctas1 == "admin" and claves_correctas2 == "CCCDDD" and claves_correctas3 == "2020":
        print("Gracias por ingresar.")
        seguir_operando = True
        while seguir_operando == True:
            codigo_golosina = int(input("Ingrese el código de la golosina que desea rellenar: "))
            cantidad_rellenar = int(input("Ingrese cuántas golosinas rellenará en la máquina: "))
            if codigo_golosina > 0 and codigo_golosina < 13 and cantidad_rellenar > 0:
                golosinas[2][codigo_golosina - 1] += cantidad_rellenar
                print(f"Usted ha ingresado {cantidad_rellenar} {golosinas[1][codigo_golosina - 1]}. La cantidad total ahora es: {golosinas[2][codigo_golosina - 1]}")
                continuar_operando = input("¿Desea seguir operando? De ser así, ingrese 'Si', o en caso contrario, ingrese 'No': ")
                if continuar_operando.lower() == "si":
                    continue
                elif continuar_operando.lower() == "no":
                    print("Volviendo al menú")
                    seguir_operando = False
                else:
                    print("Dato inválido. Volviendo al menú")
                    seguir_operando = False
            else:
                print("Ingrese un dato válido.")
    else:
        print("No tiene permiso para ejecutar la función de recarga")
        return
            
#Menú

print("¿Qué acción desea realizar?")
accion = input("Puede: 'Pedir una golosina', 'Mostrar golosinas disponibles', 'Rellenar máquina de golosinas' o 'Apagar máquina': ")
while accion.lower() != "apagar máquina":
    if accion.lower() == "pedir una golosina":
        pedirGolosina()
    elif accion.lower() == "mostrar golosinas disponibles":
        mostrarGolosinasDisponibles()
    elif accion.lower() == "rellenar máquina de golosinas":
        rellenarMaquinaGolosinas()
    else:
        print("Por favor, ingrese una acción válida.")
        
    accion = input("¿Qué acción desea realizar ahora?: 'Pedir una golosina', 'Mostrar golosinas disponibles', 'Rellenar máquina de golosinas' o 'Apagar máquina': ")

#ApagarMáquina

print("Gracias por utilizar la máquina de golosinas. Ahora verá cuáles y cuántas golosinas pidió: ")
for i in range(0, (len(golosinasPedidas))):
    print(f"[{golosinasPedidas[0][i]}][{golosinasPedidas[1][i]}][{golosinasPedidas[2][i]}]")
