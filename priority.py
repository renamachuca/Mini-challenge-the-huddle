from queue import PriorityQueue
class Cola_prioridad:
    def __init__(self):
        self.cola = PriorityQueue()

    def insertar(self, prioridad, elemento):
        self.cola.put((prioridad, elemento))

    def eliminar(self):
        if self.cola.empty():
            return None
        return self.cola.get()
    
if __name__ == "__main__":
    cola = Cola_prioridad()

    elementos = [(3, 'tarea 3'), (1, 'tarea 1'), (4, 'tarea 4'), (2, 'tarea 2'), (5, 'tarea 5')]
    for prioridad, elemento in elementos:
        cola.insertar(prioridad, elemento)

    while not cola.cola.empty():
        prioridad, elemento = cola.eliminar()
        print(f'Elemento: {elemento}, Prioridad: {prioridad}')