from datetime import datetime
import json
import csv 

def loadVehicles():
    try:
        with open('bd/vehiculos.json', 'r') as file:
            return json.load(file)
    
    except FileNotFoundError:
        return {}
    
    except json.JSONDecodeError:
        return {}
    
def saveVehicles(vehiculos):
    with open('bd/vehiculos.json', 'w') as file:
        json.dump(vehiculos, file, indent=4)

def reportExibition(report):
    date = datetime.now().strftime('%d-%m-%Y')
    with open(f'bd/report_Exibition_{date}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['codigo', 'marca', 'modelo', 'año de lanzamiento'])
        writer.writerows(report)

def sellsReport(report):
    date = datetime.now().strftime('%d-%m-%Y')
    with open(f'bd/reporte_{date}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Mes/Año", "Cantidad Vendida"])  # Escribir encabezado
        for mesAnio, cantidad in report.items():
            writer.writerow([mesAnio, cantidad])  # Escribir cada fila del reporte

    print(f"Reporte exportado a 'bd/reporte_{date}.csv' exitosamente.")