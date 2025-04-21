import json
import os
from primeraCreacion import primeraCreacion
from dibujaMapa import dibujaMapa
from interacciones import interacciones
from hazResumen import hazResumen

archivo = "estado.json"

if os.path.exists(archivo):
    # Leer el estado actual
    with open(archivo, "r") as f:
        datos = json.load(f)

    # Actualizar la ronda
    ronda = datos["ronda"]
    ac_ronda = f"acciones_{ronda}.json"
    
    ronda = ronda + 1    
    
    if os.path.exists(ac_ronda):
        # Leer las acciones de la ronda
        with open(ac_ronda, "r") as f2:
            acciones = json.load(f2)

        # Actualizar el estado según las interacciones
        estado = datos["estado"]
        jugadores = datos["jugadores"]
        estadoActualizado, jugadoresActualizado = interacciones(estado, jugadores, acciones)

        # Dibujar el mapa actualizado
        
        dibujaMapa(estadoActualizado, ronda, jugadoresActualizado)
        hazResumen(jugadoresActualizado, estadoActualizado)
        
        datosActualizado = {"estado": estadoActualizado, "jugadores": jugadoresActualizado, "ronda": ronda}
        with open('estado.json', 'w') as file:
            json.dump(datosActualizado, file)
       
    else:
        raise FileNotFoundError(f"El archivo de acciones '{ac_ronda}' no está cargado o no es la ronda correcta.")
else:
    # Crear el estado inicial si no existe
    print("No se ha encontrado el archivo de ronda actual, se crea una nueva.")
    #numeroJugadores = int(input("Número de jugadores: "))
    primeraCreacion(6)


