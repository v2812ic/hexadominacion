import json

# ronda es el número del turno recién publicado
ronda = 20

acciones = {

        #%% JUGADOR 1: PEINADO (TITO) ELIMINADO
        "Jugador1": {
            "Construir": [
            ],
            "Mover": [
            ],
            "Reclutar": [
            ],
            "Comerciar": [
            ],
            "Atacar": [
            ],
            "Cesion": [
            ],
            "RecibirRecursos":{}
        },


        #%% JUGADOR 2: SANTI (BRIFINDOR) (hecho)
        "Jugador2": {
            "Construir": [
            ],
            "Mover": [
                {"Origen": "Benabu", "Destino": "Accura", "Cantidad": 1},
                {"Origen": "Malagueta", "Destino": "Mercado", "Cantidad": 2},
                {"Origen": "Malagueta", "Destino": "Wade", "Cantidad": 1},
                {"Origen": "Leon XIII", "Destino": "Wade", "Cantidad": 3},
                {"Origen": "Brifer", "Destino": "Titotito", "Cantidad": 4},
                {"Origen": "Benabu", "Destino": "ADN", "Cantidad": 1},
            ],
            "Reclutar": [
            ],
            "Comerciar": [
            ],
            "Atacar": [
                {"Orígenes": {"Brifer": 1, "Benabu": 3, "Malagueta":1, "Tintero":1}, "Destino": "Limonar"},
            ],
            "Cesion": [
            ],
            "RecibirRecursos":{"Leon XIII": "Trigo", "Brifer": "Metal", "Titi": "Metal", "Torre" : "Trigo", "Titotito": "Madera", "Aviva": "Madera"}
        },

        #%% JUGADOR 3: OSCAR (GAMLE BY) (hecho)
        "Jugador3": {
            "Construir": [
                {"Territorio": "Periplo", "Nivel": 2},
                {"Territorio": "Peñon", "Nivel": 2},
                {"Territorio": "Larios", "Nivel": 2},
            ],
            "Mover": [
                {"Origen": "Jumanji", "Destino": "Periplo", "Cantidad": 2},
                {"Origen": "Rosario", "Destino": "Malafama", "Cantidad": 1},
                {"Origen": "David", "Destino": "Kali", "Cantidad": 1},
                {"Origen": "San Anton", "Destino": "Peñon", "Cantidad": 1},
                {"Origen": "San Anton", "Destino": "Larios", "Cantidad": 1},
                {"Origen": "Edoras", "Destino": "Larios", "Cantidad": 1},
            ],
            "Reclutar": [
                {"Territorio": "Pitu", "Cantidad": 1}, 
                {"Territorio": "Pimpi", "Cantidad": 1},  
                {"Territorio": "Victoria", "Cantidad": 1},
                {"Territorio": "Gold", "Cantidad": 1},
                {"Territorio": "Mombasa", "Cantidad": 1},
                {"Territorio": "Rincon", "Cantidad": 1},
                {"Territorio": "Fandy", "Cantidad": 1},                                 
            ],
            "Comerciar": [
            ],
            "Atacar": [
                {"Orígenes": {"Periplo": 4, "Edoras": 1, "RCC": 2}, "Destino": "Candado"},

            ],
            "Cesion": [
            ],
            "RecibirRecursos":{"Gamle By": "Madera", "El Cuervo" : "Metal", "RCC" : "Trigo", "Edoras": "Madera", "Lloyd": "Metal"}
        },

        #%% JUGADOR 4: NICO (ROHAN) ELIMINADO
        "Jugador4": {
            "Construir": [
            ],
            "Mover": [
            ],
            "Comerciar": [
            ],
            "Atacar": [
            ],
            "Cesion": [
            ],
            "RecibirRecursos":{}
        },

        #%% JUGADOR 5: JORGE (JORGE) Hecho
        "Jugador5": {
            "Construir": [
                {"Territorio": "Mosca", "Nivel": 4},
                {"Territorio": "Torrole", "Nivel": 4},
            ],
            "Mover": [
        
            ],
            "Reclutar": [
                {"Territorio": "Presentacion", "Cantidad": 2},
                {"Territorio": "Asuncion", "Cantidad": 2},
                {"Territorio": "Dundee", "Cantidad": 2},
                {"Territorio": "Skatepark", "Cantidad": 1},
                {"Territorio": "Dominos", "Cantidad": 1},
                
            ],
            "Comerciar": [

            ],
            "Atacar": [
                {"Orígenes": {"SEK": 1}, "Destino": "San Anton"},
                {"Orígenes": {"SEK": 1}, "Destino": "RCC"},
                {"Orígenes": {"Dundee": 1}, "Destino": "Edoras"},
                {"Orígenes": {"Presentacion": 1}, "Destino": "Vialia"},
                {"Orígenes": {"Presentacion": 1}, "Destino": "Titi"},
            ],
            "Cesion": [
            ],
            "RecibirRecursos":{"Torrole": "Metal", "Mosca": "Madera", "Isturk": "Madera", "Asuncion": "Piedra"}
        },

        #%% JUGADOR 6: LIMO (TIERRA SANTA)
        "Jugador6": {
            "Construir": [
                {"Territorio": "Vox", "Nivel": 2},
                {"Territorio": "Almeria", "Nivel": 2},
                {"Territorio": "Galerna", "Nivel": 2},
                {"Territorio": "Mafalda", "Nivel": 2},
            ],
            "Mover": [
                {"Origen": "Echevarria", "Destino": "4 esquinas", "Cantidad": 1},
                {"Origen": "Tejeringo", "Destino": "Mercadona", "Cantidad": 2},
                {"Origen": "Tejeringo", "Destino": "4 esquinas", "Cantidad": 2},
            ],
            "Reclutar": [
                {"Territorio": "Galerna", "Cantidad": 1},
                {"Territorio": "Jaboneros", "Cantidad": 1},
                {"Territorio": "Mafalda", "Cantidad": 1},
                {"Territorio": "Almeria", "Cantidad": 1},
                {"Territorio": "Mercadona", "Cantidad": 1},
                {"Territorio": "Vox", "Cantidad": 1},
            ],
            "Dar Baja":[
                {"Territorio": "Limonar", "Cantidad": 4},
                {"Territorio": "Candado", "Cantidad": 5},
            ],
            "Comerciar": [
            ],
            "Atacar": [
                {"Orígenes": {"Ambata": 5}, "Destino": "Accura"},  
            ],

            "Cesion": [
            ],
            "RecibirRecursos":{"Lagarillo": "Metal", "Jerusalen" : "Metal", "Pistas" : "Metal", "Mercadona": "Metal"}
        },

}

#%% EXPORT

nombreArchivo = f"acciones_{ronda}.json"
with open(nombreArchivo, "w") as archivo:
    json.dump(acciones, archivo)

#%% EJEMPLOS

'''
"Construir": [
    {"Territorio": "T1", "Nivel": 2},
    {"Territorio": "T2", "Nivel": 3},
    {"Territorio": "", "Nivel": 0},
    ...
]

"Mover": [
    {"Origen": "A1", "Destino": "A2", "Cantidad": 5},
    {"Origen": "B1", "Destino": "B2", "Cantidad": 3},
    {"Origen": "", "Destino": "", "Cantidad": 0},
    ...
]

"Atacar": [
    {"Orígenes": {"A1": 10, "A2": 5}, "Destino": "B1"},
    {"Orígenes": {"C1": 7}, "Destino": "D1"},
    {"Orígenes": {"": 0}, "Destino": ""},
    ...
]

"Jugador5": {
    "Construir": [
        {"Territorio": "", "Nivel": 0},
        {"Territorio": "", "Nivel": 0},
        {"Territorio": "", "Nivel": 0},
        {"Territorio": "", "Nivel": 0},
        {"Territorio": "", "Nivel": 0},
        {"Territorio": "", "Nivel": 0}
    ],
    "Mover": [
        {"Origen": "", "Destino": "", "Cantidad": 0},
        {"Origen": "", "Destino": "", "Cantidad": 0},
        {"Origen": "", "Destino": "", "Cantidad": 0},
        {"Origen": "", "Destino": "", "Cantidad": 0},
        {"Origen": "", "Destino": "", "Cantidad": 0},
        {"Origen": "", "Destino": "", "Cantidad": 0}
    ],
    "Reclutar": [
        {"Territorio": "", "Cantidad": 0},
        {"Territorio": "", "Cantidad": 0},
        {"Territorio": "", "Cantidad": 0},
        {"Territorio": "", "Cantidad": 0},
        {"Territorio": "", "Cantidad": 0},
        {"Territorio": "", "Cantidad": 0}
    ],
    "Comerciar": [
        {"Jugador": "", "Oferta": "", "Demanda": "", "CantidadOferta": 0, "CantidadDemanda": 0},
        {"Jugador": "", "Oferta": "", "Demanda": "", "CantidadOferta": 0, "CantidadDemanda": 0},
        {"Jugador": "", "Oferta": "", "Demanda": "", "CantidadOferta": 0, "CantidadDemanda": 0},
        {"Jugador": "", "Oferta": "", "Demanda": "", "CantidadOferta": 0, "CantidadDemanda": 0},
        {"Jugador": "", "Oferta": "", "Demanda": "", "CantidadOferta": 0, "CantidadDemanda": 0},
        {"Jugador": "", "Oferta": "", "Demanda": "", "CantidadOferta": 0, "CantidadDemanda": 0}
    ],
    "Mover capital": {
        "Origen": "", "Destino": ""
    },
    "Atacar": [
        {"Orígenes": {"": 0}, "Destino": ""},
        {"Orígenes": {"": 0}, "Destino": ""},
        {"Orígenes": {"": 0}, "Destino": ""},
        {"Orígenes": {"": 0}, "Destino": ""},
        {"Orígenes": {"": 0}, "Destino": ""},
        {"Orígenes": {"": 0}, "Destino": ""}
    ],
    "Recibir recursos": [
        {"Territorio": ""},
        {"Territorio": ""},
        {"Territorio": ""},
        {"Territorio": ""},
        {"Territorio": ""},
        {"Territorio": ""}
    ],
    "Cesion": [
        {"Cedido": "", "Destinatario": ""},
        {"Cedido": "", "Destinatario": ""},
        {"Cedido": "", "Destinatario": ""},
        {"Cedido": "", "Destinatario": ""},
        {"Cedido": "", "Destinatario": ""},
        {"Cedido": "", "Destinatario": ""}
    ],
    "RecibirRecursos": {"Ciudad": "Recurso", "Ciudad" : "Recurso"...}
},
'''
