from datetime import datetime
import json

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

def sellsReport(report):
    date = datetime.now().strftime('%d-%m-%Y')
    with open(f'bd/reporte_{date}.json', 'w') as file:
        json.dump(report, file, indent=4)