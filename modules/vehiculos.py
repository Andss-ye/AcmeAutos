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

        print(f"Se registro correctamente el vehiculo {modelo}")
        return vehiculos
    
    else:
        print("No se pudo registrar este vehiculo por que ya se encuentra registrado")
        return vehiculos