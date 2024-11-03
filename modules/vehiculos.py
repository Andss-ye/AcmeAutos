from datetime import datetime

def registrarVehiculo(vehiculos):
    codigo = str(input("\nEscriba el codigo del vehiculo: "))
    marca = input("\nEscriba la marca del vehiculo: ")
    modelo = input("\nEscriba el modelo del vehiculo: ")
    anioLanzamiento = int(input("\nEscriba el año de lanzamiento del vehiculo: "))

    if codigo not in vehiculos:
        vehiculos[codigo] = {
            "marca": marca,
            "modelo": modelo,
            "año lanzamiento": anioLanzamiento,
            "ventas": []
        }

        print(f"\nSe registro correctamente el vehiculo {modelo}")
        return vehiculos
    
    else:
        print("\nNo se pudo registrar este vehiculo por que ya se encuentra registrado")
        return vehiculos
    
def registrarVentas(vehiculos):
    codigo = str(input("\nEscriba el codigo del vehiculo: "))
    fecha = input("\nIngrese la fecha de la venta del vehiculo (DD/MM/YYYY): ")

    while True:
        try:
            fecha = datetime.strptime(fecha, "%d/%m/%Y").strftime("%d/%m/%Y")
            break
        except ValueError:
            fecha = input("Formato de fecha invalido. Asegúrate de usar el formato DD/MM/YYYY: ")

    cantidad = int(input("\nIngrese la cantidad vendida: "))
    
    if codigo in vehiculos:
        vehiculos[(codigo)]["ventas"].append({
            "fecha": fecha,
            "cantidad": cantidad
        })

        print(f"\nSe registro correctamente la venta de {vehiculos[codigo]["modelo"]}")
        return vehiculos
    
    else:
        print("\nNo se pudo registrar esta venta por que no exite ese vehiculo")
        return vehiculos
    
def vehiculosExhibicion(vehiculos):
    report = []
    print(f'CODIGO'.ljust(15) + 'MARCA'.ljust(15) + 'MODELO'.ljust(25) + 'AÑO DE LANZAMIENTO'.ljust(10))
    for codigo, vehiculo in vehiculos.items():
        print(f'{str(codigo).ljust(15)}{str(vehiculo['marca']).ljust(15)}{str(vehiculo['modelo']).ljust(25)}{str(vehiculo['año lanzamiento']).ljust(15)}')
        report.append([codigo, vehiculo['marca'], vehiculo['modelo'], vehiculo['año lanzamiento']])

    return report
