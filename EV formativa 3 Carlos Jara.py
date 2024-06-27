import csv
import time
import os

try:
    with open ("RegistroTrabajadores.csv","x") as registro:
        registroW = csv.writer(registro)
        registroW.writerow(["Trabajador", " Cargo", " Sueldo Bruto", " Desc. Salud", " Desc. AFP", " Liquido a pagar"])
        print("Creando registro de trabajadores... Cargando...")
except FileExistsError:
    print("Registro ya existente... Cargando...")


with open ("RegistroTrabajadores.csv", "r", newline="") as registro:
    registroR = csv.reader(registro)
    next(registroR)

def reg():
            trab = input("Ingrese datos del trabajador\nIngrese nombre y apellido del trabajador: ")
            cargo = input("Ingrese cargo del trabajador (CEO, Desarrollador o Analista de datos): ")
            bruto = int(input("Ingrese sueldo bruto: "))
            descSalud = int(input("Ingrese descuento de salud: "))
            descAFP = int(input("Ingrese descuento de AFP: "))
            liquido = bruto - (descSalud + descAFP)
            with open ("RegistroTrabajadores.csv", "a") as registro:
                registroW = csv.writer(registro)
                registroW.writerows([
                    [trab, cargo, bruto, descSalud, descAFP, liquido]
                    ])
def lista():
    time.sleep(2)
    os.system("cls")
    with open ("RegistroTrabajadores.csv", "r",newline="") as registro:
        registroR = csv.reader(registro)
        for i in registroR:
            print(*i)

def planilla():
    while True:
        try:
            time.sleep(2)
            os.system("cls")
            opL = int(input("Seleccione opción:\n1.Imprimir todos los sueldos\n2.Imprimir por cargo en especifico\n"))
            if opL == 1:
                with open ("RegistroTrabajadores.csv", "r", newline="") as registro:
                    registroR = csv.reader(registro)
                    next(registroR)
                    for i in registroR:
                        print(i)            
                    break
            elif opL == 2:
                while  True:
                    try:
                        opC = int(input("Seleccione cargo a imprimir sueldos:\n1. CEO\n2.Desarrollador\n3.Analista de datos\n"))
                        if opC == 1:
                            with open ("Sueldos.txt", "w") as sueldos:
                                
                                sueldos.write()
                        elif opC == 2:
                            print()
                        elif opC == 3:
                            print()
                        else:
                            print("Ingrese un número entre (1-3)")
                    except ValueError:
                        print("Valor ingresado incorrecto, vuelva a intentarlo.")
            else:
                print("Ingrese un número entre (1-2)")
        except ValueError:
            print("Valor ingresado incorrecto, vuelva a intentarlo.")
def menu():
    while True:
        try:
            op = int(input("Ingrese una opción\n1.Registrar trabajador\n2.Listar todos los trabajadores\n3.Imprimir planilla de sueldos\n4.Salir del programa\n"))
            if op == 1:
                reg()
            elif op == 2:
                lista()
            elif op == 3:
                planilla()
            elif op == 4:
                print("Gracias por usar el programa.")
                break
            else:
                print("Ingrese un número entre (1-4)")
        except ValueError:
            print("Valor ingresado incorrecto, vuelva a intentarlo.")

menu()