def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return True
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return False
lista_ordenada = [100, 110, 120, 130, 140, 150, 160, 170, 180, 200]
elemento_buscado = 200
if busqueda_binaria(lista_ordenada, elemento_buscado):
    print(f"El elemento {elemento_buscado} está en la lista.")
else:
    print(f"El elemento {elemento_buscado} no está en la lista.")
