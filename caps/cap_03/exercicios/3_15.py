#para cada estado teremos 2 sucessores:
#2k e 2k+1

import networkx as nx
from collections import deque

#letra A
def construir_estados(limite):

    estados_sucessores = {}

    for k in range(1, limite+1):
        esq = 2*k
        dir = 2*k + 1

        sucessores = []

        if esq <= limite:
            sucessores.append(esq)

        if dir <= limite:
            sucessores.append(dir)

        estados_sucessores[k] = sucessores
    
    return estados_sucessores

#estados = construir_estados(15)
#for estado, filhos in estados.items():
#    print(f"{estado} -> {filhos}")


############################
#letra B
import networkx as nx

def construir_grafo(limite):
    
    G = nx.Graph()

    for k in range(1, limite + 1):

        G.add_node(k)

        esq = 2 * k
        dir = 2 * k + 1

        if esq <= limite:
            G.add_edge(k, esq, weight=1)

        if dir <= limite:
            G.add_edge(k, dir, weight=1)

    return G

        
        
G = construir_grafo(15)

inicio = 1
objetivo = 11

visitados_larg = [inicio]

for pai, filho in nx.bfs_edges(G, source=inicio):
    visitados_larg.append(filho)
    if filho == objetivo:
        break

#print("Ordem de visita Busca Larg. :", visitados_larg)

visitados_prof = [inicio]

for pai, filho in nx.dfs_edges(G, source=inicio):
    visitados_prof.append(filho)
    if filho == objetivo:
        break

#print("Ordem de visita Busca Prof. :", visitados_prof)

def iddfs_networkx(G, inicio, objetivo, limite_max):
    for limite in range(limite_max + 1):
        predecessores = nx.dfs_predecessors(
            G,
            source=inicio,
            depth_limit=limite
        )

        # Se o objetivo foi alcançado nesta iteração
        if objetivo in predecessores or objetivo == inicio:
            # Reconstrói caminho
            caminho = [objetivo]
            atual = objetivo

            while atual != inicio:
                atual = predecessores[atual]
                caminho.append(atual)

            return list(reversed(caminho)), limite

    return None, None

caminho, profundidade = iddfs_networkx(
    G,
    inicio=inicio,
    objetivo=objetivo,
    limite_max=10
)

#print("Ordem de visita Busca Prof. Iterat.:", caminho)


#############################
#LETRA C

busca_bidirecional = nx.bidirectional_shortest_path(G, inicio, objetivo)
print(list(busca_bidirecional))
