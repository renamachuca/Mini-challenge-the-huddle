class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    def imprimir_orden(self):
        self._imprimir_orden_recursivo(self.raiz)
        print()

    def _imprimir_orden_recursivo(self, nodo):
        if nodo is not None:
            self._imprimir_orden_recursivo(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._imprimir_orden_recursivo(nodo.derecha)

if __name__ == "__main__":
    arbol = ArbolBinario()

    elementos = [25, 66, 24, 10, 9, 5]
    for elemento in elementos:
        arbol.insertar(elemento)
    
    print("Arbol en orden: ")
    arbol.imprimir_orden()