import matplotlib.pyplot as plt
import numpy as np

# Función para rotar un punto alrededor de un centro dado
def rotate_point(point, angle, center=(0, 0)):
    angle_rad = np.radians(angle)
    x, y = point
    cx, cy = center
    x_new = (x - cx) * np.cos(angle_rad) - (y - cy) * np.sin(angle_rad) + cx
    y_new = (x - cx) * np.sin(angle_rad) + (y - cy) * np.cos(angle_rad) + cy
    return x_new, y_new

# Generar vértices de un hexágono regular centrado en el origen
hexagon_vertices = []
for i in range(6):
    angle_deg = 60 * i + 30  # Rotación inicial de 30 grados
    angle_rad = np.radians(angle_deg)
    hexagon_vertices.append((np.cos(angle_rad), np.sin(angle_rad)))

# Agregar el primer vértice al final para cerrar el hexágono
hexagon_vertices.append(hexagon_vertices[0])

# Calcular puntos medios de cada lado
midpoints = []
for i in range(len(hexagon_vertices) - 1):
    x1, y1 = hexagon_vertices[i]
    x2, y2 = hexagon_vertices[i + 1]
    midpoints.append(((x1 + x2) / 2, (y1 + y2) / 2))

# Configurar el gráfico
fig, ax = plt.subplots(figsize=(50, 50))
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Dibujar el hexágono
hex_x, hex_y = zip(*hexagon_vertices)
ax.plot(hex_x, hex_y, color='black', lw=1.5)

# Dibujar las líneas desde los puntos medios hacia el centro
center = (0, 0)
colors = ["#BAE1FF", "#FFB3BA","#D7BAFF","#FFDFBA","#FFFFBA","#B9FBC0"]
for i, midpoint in enumerate(midpoints):
    x, y = zip(midpoint, center)
    ax.plot(x, y, color='black', lw=1)
    ax.fill([midpoint[0], center[0], hexagon_vertices[i][0]], 
            [midpoint[1], center[1], hexagon_vertices[i][1]], 
            color=colors[i], alpha=0.6)

# Mostrar el gráfico
plt.show()
