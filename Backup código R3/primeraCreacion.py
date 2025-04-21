from dibujaMapa import dibujaMapa
import random 
import json
from hazResumen import hazResumen

def primeraCreacion(numeroJugadores):   
    if numeroJugadores == 6:

        # Generar estado dinámico para 91 hexágonos
        territorios = [
        "Mosca",  "Calderón", "Cerrado", "Espigon", "Almeria", "Lagarillo", "Elcano", "Sebastian", "Juan", 
        "Jaboneros", "Mafalda", "Vox", "Galerna",  "Cariñoso","Miguelito",  "Jorge", "Merlo", 
        "Ancla", "Jerusalen", "Cremades", "Playa", "Cocodrilo", "Tomillo", "Chancla", 
        "Verdes", "Pistas", "Sta Gema", "Tejeringo", "Echevarria", "Ambata", "Rosario", "Dundee", "Dominos", 
        "Isturk", "BBVA", "Delgado", "Mercadona", "Tritonda", "Pomodoro", "Accura", 
        "Lloyd", "David", "Edoras", "Skatepark", "SEK", "Asuncion", "4 esquinas", "Wade", "Titotito", 
        "Mercado", "Aviva", "Fandy", "Pimpi", "Candado", "RCC", "Mombasa", 
        "Presentacion", "Leon XIII", "Tintero", "Siglo XXI", "ADN", "Pitu", "Jumanji", 
        "Periplo", "Kali", "Titi", "Vialia", "Limonar", "Malagueta", "Wahaha", "Hicosol", 
        "Rocking", "Gamle By", "Anahis", "Bubbles", "Brifer", "Benabu", "Leoni", 
        "Peñon", "Larios", "Gold", "Malafama", "Mandala", "Anden", "LG Cafe", 
        "El Cuervo", "El Moral", "Victoria", "Rincon",  "Del Mar", "Torre"
        ]
        
        c3 = ["Lagarillo", "Mosca", "Aviva", "Lloyd", "El Cuervo", "Torre"]
        c2 = ["Cariñoso", "Cocodrilo", "Tomillo", "Pitu", "Hicosol", "Jumanji", "Malafama", "Rincon", "Victoria", "Wahaha", "Leoni", "Malagueta", "Playa", "Ambata", "Echevarria", "Espigon", "Cerrado", "Jaboneros", "4 esquinas", "Presentacion", "Mombasa", "SEK", "BBVA", "Delgado"]
        c5 = ["Asuncion"]
        c4 = ["Pistas", "Mercadona", "Leon XIII", "Titi", "RCC", "Isturk"]       
        c = c3 + c4 + c5
        
        recursos = ["Trigo", "Metal", "Madera", "Piedra"]
        
        
        radius = 6  # Rango del mapa hexagonal
        coordenadas = []  # Lista para almacenar las coordenadas
        for q in range(-radius + 1, radius):
            for r in range(-radius + 1, radius):
                if abs(q + r) < radius:
                    coordenadas.append((q, r))
                    
        if len(coordenadas) < len(territorios):
            raise ValueError("No hay suficientes coordenadas para todos los territorios.")
        # Cosa que me ha dicho chatGPT
        
        
        estado = {}
        
        for i, territorio in enumerate(territorios):
            q, r = coordenadas[i]
            estado[territorio] = { 
                "propietario": "Neutral",
                "nivel": 2 if territorio in c2 else 3 if territorio in c3 else 4 if territorio in c4 else 5 if territorio in c5 else 1,
                "soldados": 0,
                "recurso": "Ciudad" if territorio in c else random.choice(recursos),
                "nombre": territorio,
                "coordenadas": (q, r)
                    
            }
        
        # Determino las casillas iniciales de los jugadores
        # Como está creado el código, los nombres son siempre en el mismo sitio
        # Aquí me he equivocado y si no quieres jugar con esta lista de nombre hay que hacer un cambio a los keys. de momento funciona asi que no se toca
        #Jugador 1
        cj1 = estado["Titotito"]
        cj1["propietario"] = "Jugador1"
        cj1["nivel"] = 3
        cj1["soldados"] = 5
        cj1["recurso"] = "Capital"
        
        #Jugador 2
        cj1 = estado["Brifer"]
        cj1["propietario"] = "Jugador2"
        cj1["nivel"] = 3
        cj1["soldados"] = 5
        cj1["recurso"] = "Capital"
        
        #Jugador 3
        cj1 = estado["Gamle By"]
        cj1["propietario"] = "Jugador3"
        cj1["nivel"] = 3
        cj1["soldados"] = 5
        cj1["recurso"] = "Capital"
        
        #Jugador 4
        cj1 = estado["Edoras"]
        cj1["propietario"] = "Jugador4"
        cj1["nivel"] = 3
        cj1["soldados"] = 5
        cj1["recurso"] = "Capital"
        
        #Jugador 5
        cj1 = estado["Jorge"]
        cj1["propietario"] = "Jugador5"
        cj1["nivel"] = 3
        cj1["soldados"] = 5
        cj1["recurso"] = "Capital"
        
        #Jugador 6
        cj1 = estado["Jerusalen"]
        cj1["propietario"] = "Jugador6"
        cj1["nivel"] = 3
        cj1["soldados"] = 5
        cj1["recurso"] = "Capital"
        
        
        jugadores = {
            "Jugador1": {
                "Piedra": 50,
                "Madera": 50,
                "Metal": 50,
                "Trigo": 50,
                "Eliminado": 0,
                "Soldados": 5,
                "Puntos": 0,
                "Nombre": "Tito",
                "Acumulado": 0
                },
            "Jugador2": {
                "Piedra": 50,
                "Madera": 50,
                "Metal": 50,
                "Trigo": 50,
                "Eliminado": 0,
                "Soldados": 5,
                "Puntos": 0,
                "Nombre": "Brifindor",
                "Acumulado": 0
                },
            "Jugador3": {
                "Piedra": 50,
                "Madera": 50,
                "Metal": 50,
                "Trigo": 50,
                "Eliminado": 0,
                "Soldados": 5,
                "Puntos": 0,
                "Nombre": "Gamle By",
                "Acumulado": 0
                },
            "Jugador4": {
                "Piedra": 50,
                "Madera": 50,
                "Metal": 50,
                "Trigo": 50,
                "Eliminado": 0,
                "Soldados": 5,
                "Puntos": 0,
                "Nombre": "Rohan",
                "Acumulado": 0
                },
            "Jugador5": {
                "Piedra": 50,
                "Madera": 50,
                "Metal": 50,
                "Trigo": 50,
                "Eliminado": 0,
                "Soldados": 5,
                "Puntos": 0,
                "Nombre": "Jorge",
                "Acumulado": 0
                },
            "Jugador6": {
                "Piedra": 50,
                "Madera": 50,
                "Metal": 50,
                "Trigo": 50,
                "Eliminado": 0,
                "Soldados": 5,
                "Puntos": 0,
                "Nombre": "Tierra Santa",
                "Acumulado": 0
                },
            }
        
        dibujaMapa(estado, "0", jugadores)
        hazResumen(jugadores, estado)
        
        datos = {"estado": estado, "jugadores": jugadores, "ronda": 0}
        with open('estado.json', 'w') as file:
            json.dump(datos, file)
        
    else:
       raise Exception(f"El juego no está diseñado para {numeroJugadores} jugadores")
    
        
        
