def dfs(grafo, nodo, recorridos):
    if nodo not in recorridos:
        print(nodo, end=' ')
        recorridos.add(nodo)

        for vecino in grafo[nodo]:
            dfs(grafo, vecino, recorridos)

grafo = {
    0: [0, 1],
    1: [2, 3, 4],
    2: [1],
    3: [0],
    4: [0]
}
recorridos = set()
print("Recorrido DFS a partir del nodo 0:")
dfs(grafo, 0, recorridos)
