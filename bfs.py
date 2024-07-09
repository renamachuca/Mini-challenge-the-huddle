def bfs(grafo, nodo_inicio):
    cola = [nodo_inicio]
    recorridos = set()
    while cola:
        nodo = cola.pop(0)
        if nodo not in recorridos:
            print(nodo, end=' ')
            recorridos.add(nodo)
            for vecino in grafo[nodo]:
                if vecino not in recorridos:
                    cola.append(vecino)
grafo = {
    0: [1, 2],
    1: [0, 3, 2],
    2: [0],
    3: [1],
    4: [1]
}   


print('Recorrido BFS a partir del nodo 0:')
bfs(grafo,0)