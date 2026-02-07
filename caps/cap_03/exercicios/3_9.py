import networkx as nx
from collections import deque

ACOES = [
    (1,0),
    (2,0),
    (0,1),
    (0,2),
    (1,1)
]

def acao(estado):
    M, C, B = estado

    acoes_sucessoras = []

    for acao in ACOES:

        if B == "E":
            nova_posi_M = M - acao[0]
            nova_posi_C = C - acao[1]
            nova_posi_B = "D"
        else:
            nova_posi_M = M + acao[0]
            nova_posi_C = C + acao[1]
            nova_posi_B = "E"

        
        if nova_posi_M < 0 or nova_posi_C < 0 or nova_posi_M > 3 or nova_posi_C > 3:
            continue

        if nova_posi_M > 0 and nova_posi_M < nova_posi_C:
            continue

        M_dir = 3 - nova_posi_M
        C_dir = 3 - nova_posi_C

        if M_dir > 0 and M_dir < C_dir:
            continue

        acoes_sucessoras.append((nova_posi_M,nova_posi_C,nova_posi_B))

    return acoes_sucessoras


def construir_grafo():
    G = nx.Graph()

    estado_inicial = (3,3,"E")
    fila = deque([estado_inicial])

    visitados = {estado_inicial}

    while fila:
        estado = fila.popleft()
        G.add_node(estado)
        
        for sucessor in acao(estado=estado):

            G.add_edge(estado,sucessor,weight=1)

            if sucessor not in visitados:
                visitados.add(sucessor)
                fila.append(sucessor)
    return G

G = construir_grafo()


def heuristica(estado,objetivo):
    
    M,C,B = estado

    pessoas = M+C

    if pessoas == 0:
        return 0
    
    custo = (pessoas +1) // 2

    if B == "D":
        custo += 1

    return custo


inicio = (3,3, "E")
objetivo = (0,0, "D")

caminho = nx.astar_path(
    G,
    source=inicio,
    target=objetivo,
    heuristic=heuristica,
    weight="weight"
)

custo = nx.astar_path_length(
    G,
    source=inicio,
    target=objetivo,
    heuristic=heuristica,
    weight="weight"
)

print("Caminho encontrado:", caminho)
print("Custo total:", custo)


inicio = (3,3, "E")
objetivo = (0,0, "D")

caminho = nx.dijkstra_path(G, inicio, objetivo, weight="weight")
print(f"O caminho de menor custo de {inicio} para {objetivo} é: {caminho}")
custo = nx.dijkstra_path_length(G, source=inicio, target=objetivo, weight='weight')
print(f"O custo total do caminho é: {custo}")
