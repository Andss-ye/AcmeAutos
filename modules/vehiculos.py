def registrarVehiculo(vehiculos):
    codigo = str(input("\nEscriba el codigo del vehiculo: "))
    marca = input("\nEscriba la marca del vehiculo: ")
    modelo = input("\nEscriba el modelo del vehiculo: ")
    anioLanzamiento = int(input("\nEscriba el año de lanzamiento del vehiculo: "))

    if codigo not in vehiculos:
        vehiculos[str(codigo)] = {
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
    codigo = int(input("\nEscriba el codigo del vehiculo: "))
    fecha = input("\nIngrese la fecha de la venta de los vehiculo: ")
    cantidad = int(input("\nIngrese la cantidad vendida: "))
    
    if codigo in vehiculos:
        vehiculos[str(codigo)]["venta"].append({
            "fecha": fecha,
            "cantidad": cantidad
        })

        print(f"\nSe registro correctamente la venta de {vehiculos["codigo"]["modelo"]}")
        return vehiculos
    
    else:
        print("\nNo se pudo registrar esta venta por que no exite ese vehiculo")
        return vehiculos