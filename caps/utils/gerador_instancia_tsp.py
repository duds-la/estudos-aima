import random
import math

class Cidade:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, outra):
        return math.sqrt((self.x - outra.x)**2 + (self.y - outra.y)**2)

    def __repr__(self):
        return f"({self.x:.3f}, {self.y:.3f})"


def gerar_tsp(n_cidades):
    cidades = []
    
    for _ in range(n_cidades):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        cidades.append(Cidade(x, y))
    
    return cidades

