import os
import json
os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)
    
empleados = cargar_json('./CRUD/empleado.json')

print(empleados)