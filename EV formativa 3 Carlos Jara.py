import csv
import time
import os

Cargos = ["CEO", "Desarrollador", "Analista de datos"]

try:
    with open ("RegistroTrabajadores.csv","x") as registro:
        registroW = csv.writer(registro)
        registroW.writerow(["Trabajador", " Cargo", " Sueldo Bruto", " Desc. Salud", " Desc. AFP", " Liquido a pagar"])
        print("Creando registro de trabajadores... Cargando...")
except FileExistsError:
    print("Registro ya existente... Cargando...")

def reg():
    while True:
            try:
                trab = input("Ingrese datos del trabajador\nIngrese nombre y apellido del trabajador: ")
                cargo = input("Ingrese cargo del trabajador (CEO, Desarrollador o Analista de datos): ")
                if cargo not in Cargos:
                    print("Cargo ingresado inválido, vuelva a intentarlo.")
                    continue
                bruto = int(input("Ingrese sueldo bruto: "))
                if bruto <= 0:
                    print("Sueldo no puede ser menor o igual a 0, vuelva a intentarlo.")
                    continue
                descSalud = int(0.07 * bruto)
                descAFP = int(0.12 * bruto)
                liquido = bruto - (descSalud + descAFP)
                with open ("RegistroTrabajadores.csv", "a") as registro:
                    registroW = csv.writer(registro)
                    registroW.writerow([trab, cargo, bruto, descSalud, descAFP, liquido])
                print("Trabajador registrado correctamente.")
                break
            except ValueError:
                print("Valor ingresado incorrecto, vuelva a intentarlo.")

def lista():
    time.sleep(2)
    os.system("cls")
    with open ("RegistroTrabajadores.csv", "r", newline="") as registro:
        registroR = csv.reader(registro)
        cabecera = next(registroR, 0)
        print(f"{cabecera[0]:<20} {cabecera[1]:<15} {cabecera[2]:<12} {cabecera[3]:<12} {cabecera[4]:<10} {cabecera[5]:<15}")
        for i in registroR:
            print(*i)

def impPlanilla(cargo):
    with open("RegistroTrabajadores.csv", "r", newline="") as registro:
        registroR = csv.reader(registro)
        next(registroR)
        with open("Sueldos.txt", "w") as sueldos:
            sueldos.write(f"Planilla de Sueldos - {cargo}\n")
            for fila in registroR:
                    if len(fila) == 6 and fila[1] == cargo:
                        sueldos.write(f"{fila[0]:<20} {fila[1]:<15} {fila[2]:<12} {fila[3]:<12} {fila[4]:<10} {fila[5]:<15}\n")


def planilla():
    while True:
        try:
            time.sleep(2)
            os.system("cls")
            opL = int(input("Seleccione opción:\n1.Imprimir todos los sueldos\n2.Imprimir por cargo en especifico\n3.Salir\n"))
            if opL == 1:
                with open ("RegistroTrabajadores.csv", "r", newline="") as registro:
                    registroR = csv.reader(registro)
                    next(registroR)
                    for i in registroR:
                        if len(i) == 6:
                            print(f"{i[0]:<20} {i[1]:<15} {i[2]:<12} {i[3]:<12} {i[4]:<10} {i[5]:<15}\n")            
                    break
            elif opL == 2:
                while  True:
                    try:
                        opC = int(input("Seleccione cargo a imprimir sueldos:\n1. CEO\n2.Desarrollador\n3.Analista de datos\n"))
                        if opC == 1:
                            impPlanilla("CEO")
                        elif opC == 2:
                            impPlanilla("Desarrollador")
                        elif opC == 3:
                            impPlanilla("Analista de datos")
                        else:
                            print("Ingrese un número entre (1-3)")
                            continue
                    except ValueError:
                        print("Valor ingresado incorrecto, vuelva a intentarlo.")
                        continue
                    break
            elif opL == 3:
                break
            else:
                print("Ingrese un número entre (1-3)")
        except ValueError:
            print("Valor ingresado incorrecto, vuelva a intentarlo.")
def menu():
    while True:
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

menu()