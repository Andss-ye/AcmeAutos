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
    with open('bd/report_Exibition.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['codigo', 'marca', 'modelo', 'año de lanzamiento'])
        writer.writerows(report)