
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import os

from calculaPuntos import calculaPuntos

def hazResumen(jugadores, estado):
    colores_titulos = {
        "Jugador1": "#FFB3BA",  
        "Jugador2": "#BAE1FF",  
        "Jugador3": "#B9FBC0",  
        "Jugador4": "#FFFFBA",  
        "Jugador5": "#FFDFBA",  
        "Jugador6": "#D7BAFF", 
    }
    
    # Directorio de salida
    output_dir = "resumenes_jugadores"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generar imágenes
    for jugador, datos in jugadores.items():
        
        soldados = 0
        # Calcula la cantidad de soldados
        for territorio, datosHex in estado.items():
            if datosHex["propietario"] == jugador:
                soldados += datosHex["soldados"]
        
        datos["Soldados"] = soldados
        
        puntos = calculaPuntos(estado, jugador, jugadores)
        datos["Puntos"] = puntos["total"]
        plt.figure(figsize=(10, 10))
        plt.axis("off")  # No mostrar los ejes
    
        if datos["Eliminado"]:
            # Si el jugador está eliminado
            plt.text(0.5, 0.5, "ELIMINADO", color="black", fontsize=40, ha="center", va="center")
        else:
            # Texto con información del jugador
            resumen = (
                f"Puntos Totales: {puntos['total']}\n\n"
                f"  - Puntos Territoriales: {puntos['territoriales']}\n"
                f"  - Puntos de Economía: {puntos['recursos']}\n"
                f"  - Puntos Militares: {puntos['soldados']}\n"
                f"  - Puntos de Cultura: {puntos['acumulado']}\n\n"
                f"Piedra: {datos['Piedra']}\n\n"
                f"Madera: {datos['Madera']}\n\n"
                f"Metal: {datos['Metal']}\n\n"
                f"Trigo: {datos['Trigo']}\n\n"
                f"Soldados: {datos['Soldados']}\n\n"
            )
            plt.text(0.5, 0.35, resumen, color="black", fontsize=20, ha="center", va="center")
    
        # Título con borde negro alrededor de las letras
        titulo = plt.text(0.5, 0.8,
            datos["Nombre"], 
            color=colores_titulos.get(jugador, "black"), 
            fontsize=50, 
            fontweight="bold", ha="center", va="center"
        )
        # Aplicar el borde negro
        titulo.set_path_effects([
            path_effects.Stroke(linewidth=3, foreground='black'),  # Contorno negro
            path_effects.Normal()  # Texto normal encima del contorno
        ])
    
        # Guardar la imagen
        filepath = os.path.join(output_dir, f"{jugador}.png")
        plt.savefig(filepath, bbox_inches="tight")
        plt.show()
        plt.close()

