def bfs_camino_corto(grafo, inicio, objetivo):
    cola = [(inicio, [inicio])]
    recorridos = set()
    while cola:
        (nodo, camino) =  cola.pop(0)
        if nodo not in recorridos:
            recorridos.add(nodo)
            if nodo == objetivo:
                return camino
            for vecino in grafo[nodo]:
                if vecino not in recorridos:
                    cola.append((vecino, camino + [vecino]))
    return None

grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1, 4],
    4: [1, 2, 3]
}

nodo_inicio = int(input('Ingrese el nodo que quieres iniciar (0 a 4)'))
nodo_objetivo = int(input('Ingresa el nodo que quieres como objetivo (0 a 4)'))

camino = bfs_camino_corto(grafo, nodo_inicio, nodo_objetivo)

if camino:
    print(f"El camino mas corto desde {nodo_inicio} hasta el nodo objetivo {nodo_objetivo} es: {camino}")
else:
    print(f'no hay caminos desde el nodo de inicio {nodo_inicio} hasta el nodo objetivo {nodo_objetivo}')