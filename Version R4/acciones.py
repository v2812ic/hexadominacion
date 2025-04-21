import json

# ronda es el número del turno recién publicado
ronda = 3

acciones = {

        #%% JUGADOR 1: PEINADO (TITO)
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


        #%% JUGADOR 2: SANTI (BRIFINDOR)
        "Jugador2": {
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

        #%% JUGADOR 3: OSCAR (GAMLE BY)
        "Jugador3": {
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

        #%% JUGADOR 4: NICO (ROHAN)
        "Jugador4": {
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

        #%% JUGADOR 5: JORGE (JORGE)
        "Jugador5": {
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

        #%% JUGADOR 6: LIMO (TIERRA SANTA)
        "Jugador6": {
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
