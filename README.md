# HexaDominación

**Versión 1.4**  
Juego de estrategia militar y gestión de recursos, diseñado para desafiar la moralidad de tus decisiones y tu sed de conquista.

## 📜 Disclaimer

HexaDominación ha sido desarrollado por una sola persona con fines lúdicos, en un tiempo reducido. Pueden existir bugs y el administrador se reserva el derecho de detener o reiniciar la simulación en caso de errores catastróficos. ¡Gracias por jugar!

---

## 🧭 Introducción

¡Bienvenido a HexaDominación! Un juego donde deberás liderar un ejército, administrar recursos y conquistar territorios hexagonales. ¿Serás el imperio dominante al finalizar la partida?

---

## 🏆 Objetivo del Juego

Ganar acumulando la mayor cantidad de **puntos al finalizar la ronda 50** (puede extenderse por votación). Existen 4 ramas de puntuación:

- **Militar:** 5 puntos por soldado.
- **Económica:** 1 punto por recurso.
- **Territorial:** Puntos según nivel de hexágono (200–600) + bonus por ciudades/capitales.
- **Cultural:** Puntos fijos por ciudad/capital por ronda y conquistas importantes.

---

## 🗺️ El Mapa

- 91 hexágonos de distintos niveles (1 a 5).
- Generado pseudo-aleatoriamente, con ubicaciones simétricas de capitales y ciudades.
- Cada jugador comienza con una capital de nivel 3.
- La capital puede moverse (si el destino es una ciudad de nivel 4 o superior).
- Si pierdes tu capital, te rindes y pierdes todo tu territorio.

---

## 🔧 Recursos

Tipos: trigo, madera, piedra, metal, ciudad.  
Cada hexágono genera recursos por ronda según su nivel (rango de 4 a 23 unidades).  
Límite: **400 por tipo**.  
Las ciudades generan el recurso que el jugador elija cada ronda.

---

## 🪖 Ejército

Solo hay **infantería**. Puedes reclutar o dar de baja soldados cada turno usando recursos.

---

## 💱 Comercio y Alianzas

- El comercio es libre pero debe ser **mutuamente notificado**.
- Las alianzas son verbales. No existen contratos vinculantes.
- Cada recurso comerciado otorga 1 punto de cultura.

---

## 🎯 Acciones por Turno

Cada ronda permite ejecutar las siguientes acciones (en orden):

1. Comerciar
2. Construir
3. Reclutar/Dar de baja soldados
4. Mover infantería
5. Mover la capital
6. Atacar
7. Recibir recursos
8. Rendirse o ceder territorios

Si no tienes recursos suficientes para una acción, se cancela automáticamente.

---

## ⚔️ Combate

- Solo puedes atacar desde hexágonos adyacentes.
- Puedes coordinar ataques desde múltiples hexágonos.
- **Defensas** se activan automáticamente si hay recursos.
- **Resultado de combate:** Se lanzan dados de 6 caras por soldado atacante y defensor. Si el ataque supera al defensor, el hexágono se conquista.

---

## 📦 Recursos por Acción

### Construcción

| De | A | Piedra | Madera | Metal |
|----|---|--------|--------|-------|
| 1  | 2 | 15     | 15     | 0     |
| 2  | 3 | 30     | 20     | 15    |
| 3  | 4 | 60     | 40     | 25    |
| 4  | 5 | 100    | 70     | 40    |

### Reclutar/Dar de Baja

| Acción         | Trigo | Madera | Metal |
|----------------|-------|--------|-------|
| Reclutar       | 2     | 4      | 2     |
| Dar de baja    | +2    | 0      | +2    |

### Ataques

| Rol       | Trigo | Madera | Recurso especial |
|-----------|-------|--------|------------------|
| Atacante  | 4     | 3      | 4 Metal          |
| Defensor  | 3     | 2      | 2 Piedra         |

### Mover Capital

| Piedra | Madera | Metal |
|--------|--------|-------|
| 60     | 30     | 20    |

---

## 🙋 Rendirse y Ceder Territorios

Puedes rendirte antes de perder tu capital. Al rendirte, puedes ceder tus territorios como desees (comercio o donación). No está permitido regalar grandes porciones de territorio al jugador dominante de forma injustificada.

---

## 📌 Notas Finales

- Las decisiones deben notificarse con claridad.
- No se tolerarán trampas o manipulaciones dudosas.
- ¡Que gane el más astuto, no el más honesto!
- Está permitida la reproducción, mejora, y uso del código con fines lúdicos (NO COMERCIALES), referenciando a Víctor Rodríguez Romero como autor intelectual original. Gracias.
  - Para cargar el juego y el primer estado se realiza una ejecución del main.
  - Una vez cargado, se ha de ir editando el archivo de acciones ronda por ronda, según los ejemplos que hay en el mismo archivo.
  - Para correr una ronda se corre acciones.py y acto seguido main.py. Ya está. Para más dudas, contactar con @hexadominacion en instagram.

---

¡Disfruta conquistando en **HexaDominación**! 🛡️
