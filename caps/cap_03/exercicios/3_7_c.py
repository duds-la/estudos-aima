import matplotlib.pyplot as plt
from math import sqrt

class Vertice:
    def __init__(self, x, y, nome=None):
        self.x = x
        self.y = y
        self.nome = nome or f"({x:.2f},{y:.2f})"

    def __repr__(self):
        return self.nome

class Poligono:
    def __init__(self, vertices):
        self.vertices = vertices

PtI = Vertice(0, 0, "S")

cord = [
    (-0.05,2.253),(1.035,3.243),(1.736,2.278),(1.166,1.014),(0.125,1.268),(0.267,0.532),
    (0.274,-0.435),(3.283,0.53),(3.274,-0.43),(2.18,2.456),(1.78,0.93),(2.614,0.945),
    (2.68,1.95),(2.68,3.155),(3.425,3.236),(3.944,2.69),(3.42,1.455),(3.73,0.06),
    (4.347,0.67),(4.12,3.13),(5.373,3.13),(4.126,1.155),(5.364,1.16),(5.546,2.86),
    (6,3.2),(6.35,2.82),(6.2,0.93),(6.05,0.58),(5.53,1.036),(4.85,0.6),
    (4.85,-0.17),(5.425,-0.48),(6.06,-0.14)
]

PtF = Vertice(6.54, 3.114, "G")

vertices = [Vertice(x, y, f"P{i}") for i, (x, y) in enumerate(cord)]
todos_vertices = [PtI] + vertices + [PtF]

obstaculos = [
    Poligono(vertices[0:5]),
    Poligono(vertices[5:7]),
    Poligono(vertices[7:9]),
    Poligono(vertices[9:16]),
    Poligono(vertices[16:19]),
    Poligono(vertices[19:25]),
    Poligono(vertices[25:33])
]

def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)
def segmentos_intersectam(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
def cruza_poligono(v1, v2, poligono):
    verts = poligono.vertices
    n = len(verts)

    for i in range(n):
        a = verts[i]
        b = verts[(i + 1) % n]

        if a in (v1, v2) or b in (v1, v2):
            continue

        if segmentos_intersectam(v1, v2, a, b):
            return True

    return False
def visivel(v1, v2, obstaculos):
    for pol in obstaculos:
        if cruza_poligono(v1, v2, pol):
            return False
    return True
def desenhar_poligono(poligono):
    xs = [v.x for v in poligono.vertices] + [poligono.vertices[0].x]
    ys = [v.y for v in poligono.vertices] + [poligono.vertices[0].y]
    plt.plot(xs, ys, color="black", linewidth=2)
def desenhar_ambiente():
    plt.figure(figsize=(12, 6))

    # Obstáculos
    for pol in obstaculos:
        desenhar_poligono(pol)

    # Grafo de visibilidade
    for v1 in todos_vertices:
        for v2 in todos_vertices:
            if v1 != v2 and visivel(v1, v2, obstaculos):
                plt.plot([v1.x, v2.x], [v1.y, v2.y],
                         color="lightgray", linewidth=0.5)

    # Vértices
    for v in vertices:
        plt.scatter(v.x, v.y, color="gray", s=30)

    # S e G
    plt.scatter(PtI.x, PtI.y, color="green", s=100)
    plt.text(PtI.x - 0.2, PtI.y - 0.2, "S")

    plt.scatter(PtF.x, PtF.y, color="red", s=100)
    plt.text(PtF.x + 0.05, PtF.y + 0.05, "G")

    plt.axis("equal")
    plt.grid(True)
    plt.title("Polígonos, Vértices e Grafo de Visibilidade")
    plt.show()

desenhar_ambiente()
