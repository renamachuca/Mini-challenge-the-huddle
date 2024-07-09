class Cola:
    def __init__(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0
    
    def agregar_cola(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacio():
            return self.items.pop(0)
        else:
            raise IndexError('La cola esta vacia')
        
    def ver_frente(self):
        if not self.esta_vacio():
            return self.items[0]
        else:
            raise IndexError('La cola esta vacia')

if __name__ == "__main__":
    cola = Cola()
    for i in range(5):
        cola.agregar_cola(i)

    print('frente de la cola:', cola.ver_frente())
    print('desencolando elementos:')
    while not cola.esta_vacio():
        print(cola.desencolar())