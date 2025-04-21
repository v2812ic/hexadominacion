import random  

# Devuelve si un jugador tiene suficientes recursos para construir
def cumpleRequisitos(datosJugador, trigo, piedra, madera, metal):
    return datosJugador["Trigo"]  >= trigo and datosJugador["Piedra"]  >= piedra and datosJugador["Madera"] >= madera and datosJugador["Metal"] >= metal

def sonVecinos(coord1, coord2):
    q1, r1 = coord1
    q2, r2 = coord2
    return (q2, r2) in [
        (q1 + 1, r1), (q1 - 1, r1), 
        (q1, r1 + 1), (q1, r1 - 1), 
        (q1 + 1, r1 - 1), (q1 - 1, r1 + 1)
    ]

def obtenerVecinosDisponibles(coord, jugador, estado):
        """
        Obtiene los hexágonos vecinos disponibles para redistribuir soldados.
        """
        q, r = coord
        vecinos = [
            (q + 1, r), (q - 1, r),
            (q, r + 1), (q, r - 1),
            (q + 1, r - 1), (q - 1, r + 1)
        ]
        return [
            hex_nombre for hex_nombre, datos in estado.items()
            if (datos["coordenadas"][0], datos["coordenadas"][1]) in vecinos and datos["propietario"] == jugador
        ] 

def estanConectados(origen, destino, jugador, estado):
    """
    Verifica si existe un camino desde `origen` hasta `destino` que pase solo por territorios del jugador.
    """
    visitados = set()

    def dfs(celdaActual):
        if celdaActual == destino:
            return True
        visitados.add(celdaActual)

        vecinos = obtenerVecinosDisponibles(estado[celdaActual]["coordenadas"], jugador, estado)
        
        for vecino in vecinos:
            if vecino not in visitados:
                if dfs(vecino):
                    return True
        return False

    return dfs(origen)

# estado: diccionario en el que las entradas son los territorios
# su contenido es otro diccionario en el que aparece la información de los territorios:
    #"propietario"
    #"nivel"
    #"soldados"
    #"recurso"
    #"nombre"

# jugadores: diccionario en el que las entradas son los jugadores ("jugador1, jugador2, etc")
# su contenido es otro diccionario en el que aparece la información de cada jugador
    #"Piedra"
    #"Madera"
    #"Metal"
    #"Trigo"
    #"Eliminado"
    #"Soldados"
    #"Puntos"
    #"Nombre": "Imperio brutal 1" (no coincide con la key)
    #"Acumulado"
    
# acciones: diccionario en el que las entradas son los jugadores ("jugador1, jugador2, etc")
# su contenido es otro diccionario en el que aparece la serie de acciones de cada jugador
    #"Construir"
    #"Mover
    #"Reclutar
    #Comerciar
    #Mover capital
    
    #Atacar
    #Recibir recursos
    #Rendirse y ceder territorios

# Cada accion es un vector (vacio si no se realiza la accion) en el que hay otro diccionario por entrada que indica las cosas de cada accion    

def interacciones(estado, jugadores, acciones):
    # comerciar es lo que vas a recibir de qué jugador
    ordenAcciones = ["Comerciar", "Construir", "Reclutar", "Dar Baja", "Mover", "Mover capital"]
    
    for accion in ordenAcciones: # Selecciona la accion a realizar (construir, mover, etc)
        for jugador, datosJugador in jugadores.items(): # Desempaqueta el jugador que realiza la accion
            if accion in acciones[jugador]: # Comprueba si decide realizarla
                accionesJugador = acciones[jugador][accion] #Desempaqueta el diccionario de accion de jugador
                
                # Construccion
                if accion == "Construir":
                    for construccion in accionesJugador:
                        territorio = construccion["Territorio"]
                        nivel = construccion["Nivel"]
                        if nivel == estado[territorio]["nivel"] + 1 and estado[territorio]["propietario"] == jugador:
                             if nivel == 2:
                                 piedra = 15
                                 madera = 15
                                 metal = 0
                                 if cumpleRequisitos(datosJugador, 0, piedra, madera, metal):
                                     datosJugador["Piedra"] -= piedra
                                     datosJugador["Madera"] -= madera
                                     datosJugador["Metal"] -= metal
                                     estado[territorio]["nivel"] = nivel
                                     print(f"{jugador} ha construido exitosamente en {territorio} al nivel {nivel}.")
                                 else:
                                     print(f"{jugador} no tiene suficientes recursos para construir en {territorio} al nivel {nivel}.")
                             elif nivel == 3:
                                 piedra = 30
                                 madera = 20
                                 metal = 15
                                 if cumpleRequisitos(datosJugador, 0, piedra, madera, metal):
                                     datosJugador["Piedra"] -= piedra
                                     datosJugador["Madera"] -= madera
                                     datosJugador["Metal"] -= metal
                                     estado[territorio]["nivel"] = nivel
                                     print(f"{jugador} ha construido exitosamente en {territorio} al nivel {nivel}.")
                                 else:
                                     print(f"{jugador} no tiene suficientes recursos para construir en {territorio} al nivel {nivel}.")
                             elif nivel == 4:
                                 piedra = 60
                                 madera = 40
                                 metal = 25
                                 if cumpleRequisitos(datosJugador, 0, piedra, madera, metal):
                                     datosJugador["Piedra"] -= piedra
                                     datosJugador["Madera"] -= madera
                                     datosJugador["Metal"] -= metal
                                     estado[territorio]["nivel"] = nivel
                                     print(f"{jugador} ha construido exitosamente en {territorio} al nivel {nivel}.")
                                 else:
                                     print(f"{jugador} no tiene suficientes recursos para construir en {territorio} al nivel {nivel}.")
                             elif nivel == 5:
                                 piedra = 100
                                 madera = 70
                                 metal = 40
                                 if cumpleRequisitos(datosJugador, 0, piedra, madera, metal):
                                     datosJugador["Piedra"] -= piedra
                                     datosJugador["Madera"] -= madera
                                     datosJugador["Metal"] -= metal
                                     estado[territorio]["nivel"] = nivel
                                     print(f"{jugador} ha construido exitosamente en {territorio} al nivel {nivel}.")
                                 else:
                                     print(f"{jugador} no tiene suficientes recursos para construir en {territorio} al nivel {nivel}.")
                        else: 
                             print(f"{jugador} no puede construir en {territorio}. Las instrucciones no son correctas.")
                                     
                # Accion de mover              
                elif accion == "Mover": 
                    for movimiento in accionesJugador:
                        origen = movimiento["Origen"]
                        destino = movimiento["Destino"]
                        cantidad = movimiento["Cantidad"]
                        
                        # Validar propietario y conexión
                        if (estado[origen]["propietario"] == jugador and 
                            estado[destino]["propietario"] == jugador and estanConectados(origen, destino, jugador, estado)):
                            
                            moverReal = min(estado[origen]["soldados"], cantidad)
                            estado[origen]["soldados"] -= moverReal
                            estado[destino]["soldados"] += moverReal  # Si hay menos soldados de los que se indican en la orden, se mueven todos
                            
                            print(f"{jugador} ha movido {moverReal} soldados desde {origen} hacia {destino}.")
                        else:
                            print(f"{jugador} no puede mover soldados desde {origen} hacia {destino}. Las instrucciones no son correctas o los territorios no están conectados.")
                                    
                            
                #Accion de reclutar
                elif accion == "Reclutar":
                    for reclutamiento in accionesJugador:
                        territorio = reclutamiento["Territorio"]
                        cantidad = reclutamiento["Cantidad"]
                        trigo = cantidad*2
                        madera = cantidad*4
                        metal = cantidad*2
                        piedra = cantidad*0
                        if estado[territorio]["propietario"] == jugador and cumpleRequisitos(datosJugador, trigo, piedra, madera, metal):
                            estado[territorio]["soldados"] += cantidad
                            datosJugador["Trigo"] -= trigo
                            datosJugador["Piedra"] -= piedra
                            datosJugador["Madera"] -= madera
                            datosJugador["Metal"] -= metal
                            print(f"{jugador} ha reclutado {cantidad} soldados en {territorio}.")
                        else: 
                             print(f"{jugador} no puede reclutar en {territorio}. Las instrucciones no son correctas o no tiene suficientes recursos.")
                elif accion == "Dar Baja":
                    for baja in accionesJugador:
                        territorio = baja["Territorio"]
                        cantidad = baja["Cantidad"]
                        if estado[territorio]["propietario"] == jugador and estado[territorio]["soldados"] >= cantidad:
                            estado[territorio]["soldados"] -= cantidad
                            datosJugador["Trigo"] += 2
                            datosJugador["Metal"] += 2
                            print(f"{jugador} ha dado de baja {cantidad} soldados en {territorio}.")
                        else:
                            print(f"{jugador} no puede dar de baja soldados en {territorio}. Las instrucciones no son correctas.")
           
                        
                #Accion de comerciar
                elif accion == "Comerciar":
                    for comercio in accionesJugador:
                        jugadorContrario = comercio["Jugador"]
                        recursoOfrecido = comercio["Oferta"]
                        recursoDemandado = comercio["Demanda"]
                        cantidadOfrecida = comercio["CantidadOferta"]
                        cantidadDemanda = comercio["CantidadDemanda"]
                        if datosJugador[recursoOfrecido] >= cantidadOfrecida and jugadores[jugadorContrario][recursoDemandado] >= cantidadDemanda:
                            datosJugador[recursoOfrecido] -= cantidadOfrecida
                            datosJugador[recursoDemandado] += cantidadDemanda
                            jugadores[jugadorContrario][recursoDemandado] -= cantidadDemanda
                            jugadores[jugadorContrario][recursoOfrecido] += cantidadOfrecida
                            datosJugador["Acumulado"] += (cantidadDemanda + cantidadOfrecida)
                            jugadores[jugadorContrario]["Acumulado"] += (cantidadDemanda + cantidadOfrecida)
                        
                #REVISAR ACUERDOS DE COMERCIO E INCLUIR SOLAMENTE UNO DE LOS BANDOS, SI NO SE MULTIPLICA POR DOS
                        else: 
                            print(f"No se han dado instrucciones correctas en el Comercio por parte de {jugador}")
                            
                #Accion de mover la capital
                elif accion == "Mover capital":
                    origen = accionesJugador["Origen"]
                    destino = accionesJugador["Destino"]
                    trigo = 0
                    piedra = 60
                    madera = 30
                    metal = 20
                    if estado[origen]["propietario"] == jugador and estado[destino]["propietario"] == jugador and estado[destino]["nivel"] >= 4 and cumpleRequisitos(datosJugador, trigo, piedra, madera, metal) and estado[destino]["recurso"] == "Ciudad":
                       estado[origen]["recurso"] = "Ciudad"
                       estado[destino]["recurso"] = "Capital"
                       datosJugador["Trigo"] -= trigo
                       datosJugador["Piedra"] -= piedra
                       datosJugador["Madera"] -= madera
                       datosJugador["Metal"] -= metal
                    else: 
                         print(f"No se han dado instrucciones correctas en el Movimiento de la Capital por parte de {jugador}")
                       
    # ACCION DE ATAQUE
    jugadoresAleatorios = list(jugadores.keys())
    random.shuffle(jugadoresAleatorios)
    
    for jugador in jugadoresAleatorios:
        if jugador in acciones and "Atacar" in acciones[jugador]:
            ataques = acciones[jugador]["Atacar"]
            for ataque in ataques:
                origenes = ataque["Orígenes"]  # Diccionario: {origen: cantidad_soldados}
                destino = ataque["Destino"]
    
                # Validaciones iniciales
                if all(estado[origen]["propietario"] == jugador for origen in origenes) and estado[destino]["propietario"] != jugador:
                    coordDestino = estado[destino]["coordenadas"]
    
                    # Verificar vecindad para todos los hexágonos de origen
                    if all(sonVecinos(estado[origen]["coordenadas"], coordDestino) for origen in origenes):
                        totalSoldAtaque = sum(
                            min(estado[origen]["soldados"], cantidad)  # Asegurarse de no usar más soldados de los disponibles
                            for origen, cantidad in origenes.items()
                        )
    
                        trigo = totalSoldAtaque * 4
                        madera = totalSoldAtaque * 3
                        piedra = totalSoldAtaque * 0
                        metal = totalSoldAtaque * 4
    
                        # Verificar recursos suficientes
                        if cumpleRequisitos(jugadores[jugador], trigo, piedra, madera, metal):
                            # Descontar los recursos
                            jugadores[jugador]["Trigo"] -= trigo
                            jugadores[jugador]["Piedra"] -= piedra
                            jugadores[jugador]["Madera"] -= madera
                            jugadores[jugador]["Metal"] -= metal
    
                            # Calcular efectividad del ataque
                            efectividadAtaque = sum(random.randint(1, 6) for _ in range(totalSoldAtaque))
    
                            # Calcular efectividad de la defensa
                            defensores = estado[destino]["soldados"]
                            propietarioDefensor = estado[destino]["propietario"]
                            efectividadDefensa = 0
                            defensaTotal = 0
    
                            if propietarioDefensor in jugadores:
                                recursosDefensor = jugadores[propietarioDefensor]
                                trigoDisponible = recursosDefensor["Trigo"]
                                piedraDisponible = recursosDefensor["Piedra"]
                                maderaDisponible = recursosDefensor["Madera"]
    
                                trigoDefensa = 3
                                maderaDefensa = 2
                                piedraDefensa = 2
    
                                maxDefensoresTrigo = trigoDisponible // trigoDefensa
                                maxDefensoresPiedra = piedraDisponible // piedraDefensa
                                maxDefensoresMadera = maderaDisponible // maderaDefensa
                                maxDefensores = min(maxDefensoresMadera, maxDefensoresTrigo, maxDefensoresPiedra)
    
                                defensaTotal = min(maxDefensores, defensores)
    
                                recursosDefensor["Trigo"] -= trigoDefensa * defensaTotal
                                recursosDefensor["Piedra"] -= piedraDefensa * defensaTotal
                                recursosDefensor["Madera"] -= maderaDefensa * defensaTotal
    
                                efectividadDefensa = sum(random.randint(1, 6) for _ in range(defensaTotal))
    
                            # DESARROLLO DE LA BATALLA
                            
                            # El atacante gana
                            if efectividadAtaque > efectividadDefensa:
                                print(f"{jugador} conquista {destino} desde {', '.join(origenes.keys())}!")
                                                                
                                # Redistribución de defensores
                                vecinosDisponibles = obtenerVecinosDisponibles(coordDestino, propietarioDefensor, estado)
                                
                                defensaTotal -= defensaTotal //4
                                if vecinosDisponibles:
                                    for _ in range(defensaTotal):
                                        destinoVecino = random.choice(vecinosDisponibles)
                                        estado[destinoVecino]["soldados"] += 1
                                        
                                else:  
                                    print("Acorralado! No hay vecinos disponibles!")
                                estado[destino]["propietario"] = jugador
                                                                
                                # Considerar la conquista de una capital: rendición automática 
                                if estado[destino]["recurso"] == "Capital":
                                    print(f"¡El jugador {propietarioDefensor} ha sido eliminado! Su capital ha sido conquistada.")
                                    jugadores[propietarioDefensor]["Eliminado"] = True
                                    estado[destino]["recurso"] = "Ciudad"
                                    jugadores[jugador]["Acumulado"] += 300 # 300 puntos por eliminar a alguien
                                    
                                    for hexagono, datosHex in estado.items():
                                        if datosHex["propietario"] == propietarioDefensor:
                                            datosHex["propietario"] = jugador
                                            datosHex["soldados"] = 0
                                    
                                    jugadores[propietarioDefensor]["Piedra"] = 0
                                    jugadores[propietarioDefensor]["Madera"] = 0
                                    jugadores[propietarioDefensor]["Trigo"] = 0
                                    jugadores[propietarioDefensor]["Metal"] = 0
                                    
                                    
                                # Asentamiento de los atacantes
                                estado[destino]["soldados"] = totalSoldAtaque
                                
                                for origen, cantidad in origenes.items():
                                    estado[origen]["soldados"] -= min(estado[origen]["soldados"], cantidad)
                                    
                            # El defensor gana
                            else:
                                print(f"{jugador} falla en conquistar {destino}.")
                                perdidas = totalSoldAtaque//4
                                origenesLista = list(origenes.items())

                                while perdidas > 0 and origenesLista:
                                    # Mezclar aleatoriamente los orígenes en cada iteración
                                    random.shuffle(origenesLista)
                                
                                    # Aplicar una pérdida a cada origen, de forma balanceada
                                    for origen, cantidad in origenesLista:
                                        if perdidas <= 0:
                                            break
                                
                                        if estado[origen]["soldados"] > 0:  # Solo reducir si hay soldados
                                            estado[origen]["soldados"] -= 1
                                            perdidas -= 1
                                estado[destino]["soldados"] = defensaTotal
                                
                        else:
                                print(f"{jugador} no tiene suficientes recursos para atacar {destino} desde {', '.join(origenes)}.")
                    else:
                        print(f"El ataque de {', '.join(origenes)} a {destino} no es válido: no son vecinos.")
                else:
                    print(f"Ataque inválido desde {', '.join(origenes)} hacia {destino} por parte de {jugador}.")
    
    
    # ACCION DE RECIBIR RECURSOS
    for territorio, datosTerritorio in estado.items():
        propietario = datosTerritorio["propietario"]
        recurso = datosTerritorio["recurso"]
        nivel = datosTerritorio["nivel"]
        
        if propietario in jugadores:
            if recurso != "Ciudad" and recurso != "Capital":
                
                if nivel == 1:
                    recibe = random.randint(4, 6)
                elif nivel == 2:
                    recibe = random.randint(6, 10)
                elif nivel == 3:
                    recibe = random.randint(8, 12)
                elif nivel == 4:
                    recibe = random.randint(12, 16)
                elif nivel == 5:
                    recibe = random.randint(18, 23)
                
                jugadores[propietario][recurso] += recibe
                jugadores[propietario][recurso] = min(jugadores[propietario][recurso], 400)
                
            elif recurso == "Ciudad" or recurso == "Capital":
                
                puntos = 0
                recibe = 0
                
                rec = acciones[propietario]["RecibirRecursos"].get(territorio, None)
                
                if nivel == 3:
                    puntos = 30
                    recibe = random.randint(8, 12)
                    
                elif nivel == 4:
                    puntos = 50
                    recibe = random.randint(12, 16)
                    
                elif nivel == 5:
                    puntos = 75
                    recibe = random.randint(18, 23)
                
                if rec is not None:
                    jugadores[propietario][rec] += recibe    
                    jugadores[propietario][rec] = min(jugadores[propietario][rec], 400)
    # sumar puntos en acumulado
                jugadores[propietario]["Acumulado"] += puntos
           
    # ACCION DE RENDIRSE Y CEDER TERRITORIOS
    # Considerar la acción de rendirse como cesion de todos los territorios
    # Cuidado con ceder la capital
    for jugador in jugadores:
        if "Cesion" in acciones[jugador]:
            cesiones = acciones[jugador]["Cesion"]
            for cesion in cesiones:
                cedido = cesion["Cedido"]
                destinatario = cesion["Destinatario"]
                coordenadas_cedido = estado[cedido]["coordenadas"]
    
                if estado[cedido]["propietario"] == jugador and not jugadores[destinatario]["Eliminado"]:
                    # Obtener vecinos disponibles para redistribuir soldados
                    vecinos_disponibles = obtenerVecinosDisponibles(coordenadas_cedido, jugador, estado)
                    soldados_cedidos = estado[cedido]["soldados"]
                    
                    if vecinos_disponibles:
                        soldados_por_vecino = soldados_cedidos // len(vecinos_disponibles)
                        resto_soldados = soldados_cedidos % len(vecinos_disponibles)
    
                        # Distribuir soldados equitativamente entre los vecinos
                        for vecino in vecinos_disponibles:
                            estado[vecino]["soldados"] += soldados_por_vecino
    
                        # Distribuir el resto de soldados entre los primeros vecinos
                        for i in range(resto_soldados):
                            estado[vecinos_disponibles[i]]["soldados"] += 1
                    
                    # Cambiar la propiedad del territorio cedido
                    estado[cedido]["propietario"] = destinatario
                    estado[cedido]["soldados"] = 0  # Soldados ya redistribuidos
    
        # Verificar si el jugador posee al menos un territorio
        posee_territorio = any(
            datosHex["propietario"] == jugador for datosHex in estado.values()
        )
    
        # Actualizar estado del jugador basado en la posesión de territorios
        jugadores[jugador]["Eliminado"] = not posee_territorio
            
    return estado, jugadores
        
    
    
    