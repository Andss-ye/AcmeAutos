from modules.fileManager import  *
from modules.vehiculos import *

def menu():
    print("\n=========== BIENVENIDO ===========")
    print("1. Registrar vehiculo en exhibicion")
    print("2. Registrar venta de vehiculo")
    print("3. Listar vehiculos")
    print("4. Generar reporte de ventas por mes")
    print("0. Exit")
    print("=================================")
    opc = int(input("Ingrese una opcion: "))
    return opc

vehiculos = loadVehicles()

opc = 10

while opc != 0:
    try:
        opc = menu()
        if opc == 1:
            print("Registrar vehiculo en exhibicion")
            vehiculos = registrarVehiculo(vehiculos)
            saveVehicles(vehiculos)

        elif opc == 2:
            print("Registrar venta de vehiculo")
            vehiculos = registrarVentas(vehiculos)
            saveVehicles(vehiculos)

        elif opc == 3: 
            print("Listar vehiculos")
            report = vehiculosExhibicion(vehiculos)
            reportExibition(report)

        elif opc == 4:
            print("Generar reporte de ventas por mes")
        elif opc == 0:
            print("Exit")
        else:
            print("\nOpcion incorrecta, solo se permite de 0-4")

    except ValueError:
        print("\nDigite bien, solo se permiten numeros")