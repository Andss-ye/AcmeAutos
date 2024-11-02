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