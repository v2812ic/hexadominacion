import numpy as np
import matplotlib.pyplot as plt


def hex_to_cartesian(q, r, size):
    x = size * (3/2 * q)
    y = size * (np.sqrt(3) * (r + q / 2))
    return x, y

def draw_hex(ax, x, y, size, color):
    angles = np.linspace(0, 2 * np.pi, 7)
    hex_x = x + size * np.cos(angles)
    hex_y = y + size * np.sin(angles)
    ax.fill(hex_x, hex_y, color=color, edgecolor='black')

def obtener_color(propietario):
    colores_propietario = {
        "Jugador1": "#FFB3BA",  
        "Jugador2": "#BAE1FF",  
        "Jugador3": "#B9FBC0",  
        "Jugador4": "#FFFFBA",  
        "Jugador5": "#FFDFBA",  
        "Jugador6": "#D7BAFF", 
        "Neutral": "#F5F5F5"
    }
    return colores_propietario.get(propietario)

def dibujaMapa(estado, ronda, jugadores):
    def vecinos_hex(q, r):
        # Coordenadas relativas de los vecinos en un mapa hexagonal
        return [
            (q + 1, r), (q - 1, r), 
            (q, r + 1), (q, r - 1), 
            (q + 1, r - 1), (q - 1, r + 1)
        ]
    
    def arista_comun(x1, y1, x2, y2, size):
        # Encuentra la línea entre dos hexágonos
        angle = np.arctan2(y2 - y1, x2 - x1)
        offset_x = size * np.cos(angle + np.pi / 6)
        offset_y = size * np.sin(angle + np.pi / 6)
        return [(x1 + offset_x, y1 + offset_y), (x2 - offset_x, y2 - offset_y)]

    fig, ax = plt.subplots(figsize=(50, 50))
    size = 5  # Tamaño de los hexágonos
    
    radius = 6
    keys = list(estado.keys())  # Obtener las claves directamente desde el estado
    index = 0  # Índice para recorrer las claves
    
    hex_positions = {}  # Diccionario para almacenar posiciones de los hexágonos
    
    # Crear hexágonos y almacenar sus posiciones
    for q in range(-radius + 1, radius):
        for r in range(-radius + 1, radius):
            if abs(q + r) < radius:
                if index >= len(keys):
                    break
                
                key = keys[index]
                index += 1
                
                hex_data = estado[key]
                propietario = hex_data["propietario"] 
                nivel = hex_data["nivel"]
                soldados = hex_data["soldados"]
                recurso = hex_data["recurso"]
                nombre = hex_data["nombre"]
                
                # Convertir a coordenadas cartesianas
                x, y = hex_to_cartesian(q, r, size)
                hex_positions[(q, r)] = (x, y, propietario)
                
                # Dibujar hexágono
                draw_hex(ax, x, y, size, obtener_color(propietario))
                
                # Añadir información al hexágono
                ax.text(x, y, nombre, ha="center", va="center", fontsize=size*6, color="black", fontweight="bold")
                ax.text(x, y + size*0.3, f"Niv. $\\bf{{{nivel}}}$" if nivel >= 3 else f"Niv. {nivel}", ha="center", va="center", fontsize=size*6, color="black")
                if soldados > 0:
                    ax.text(x, y - size*0.3, f"{soldados}", ha="center", va="center", fontsize=size*6, color="black")
                ax.text(x, y - size*0.6, recurso, ha="center", va="center", fontsize=size*6, 
                        color="black", fontweight="bold" if recurso == "Capital" else "normal")
    
    # Dibujar bordes más gruesos entre hexágonos de diferente color
    for (q, r), (x, y, propietario) in hex_positions.items():
        for nq, nr in vecinos_hex(q, r):
            if (nq, nr) in hex_positions:
                x2, y2, vecino_propietario = hex_positions[(nq, nr)]
                if propietario != vecino_propietario:
                    # Dibujar el borde grueso en la arista compartida
                    arista = arista_comun(x, y, x2, y2, size)
                    ax.plot(
                        [arista[0][0], arista[1][0]], 
                        [arista[0][1], arista[1][1]], 
                        color='black', linewidth=4, zorder=3
                    )
    
    ax.text(0.95, 0.05, f"Turno {ronda}", ha="right", va="bottom", transform=ax.transAxes, fontsize=120, color="black", fontname="Arial")

    # Ajustar la visualización
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Mostrar el mapa hexagonal
    plt.savefig(f"Mapa turno {ronda}", bbox_inches="tight")
    plt.show()
    plt.close()

