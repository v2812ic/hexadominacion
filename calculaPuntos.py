def calculaPuntos(estado, jugador, jugadores):
    
    puntosTerritoriales = 0
    for datos in estado.values():
        if datos["propietario"] == jugador:
            nivel = datos["nivel"]
            puntosHex = (
                200 if nivel <= 3 else
                350 if nivel == 4 else
                600 if nivel == 5 else 0
                )
            if datos["recurso"] == "Ciudad" or datos["recurso"] == "Capital":
                puntosHex += 100
            puntosTerritoriales += puntosHex
            
    puntosRecursos = (1*jugadores[jugador]["Piedra"] + 
                      1*jugadores[jugador]["Trigo"] + 
                      1*jugadores[jugador]["Madera"] + 
                      1*jugadores[jugador]["Metal"])
    
    puntosSoldados = jugadores[jugador]["Soldados"] * 5
    
    puntosAcumulados = jugadores[jugador]["Acumulado"]
    
    return{
        "territoriales" : puntosTerritoriales,
        "recursos" : puntosRecursos,
        "soldados" : puntosSoldados,
        "acumulado": puntosAcumulados,
        "total" : puntosTerritoriales + puntosRecursos + puntosSoldados + puntosAcumulados}
