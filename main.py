from modules.fileManager import  *

def menu():
    print("\n=========== BIENVENIDO ===========")
    print("1. Registrar vehiculo en exhibicion")
    print("2. Registrar venta de vehiculo")
    print("3. Listar vehiculos")
    print("3. Generar reporte de ventas por mes")
    print("0. Exit")
    print("=================================")
    opc = int(input("Ingrese una opcion: "))
    return opc

vehiculos = loadVehicles()
ventas = loadSells()

opc = 10

while opc != 0:
    opc = menu()
    if opc == 1:
        print("Registrar vehiculo en exhibicion")
    elif opc == 2:
        print("Registrar venta de vehiculo")
    elif opc == 3:
        print("Listar vehiculos")
    elif opc == 4:
        print("Generar reporte de ventas por mes")
    elif opc == 0:
        print("Exit")
    else:
        print("Opcion incorrecta")