def pedir_lista():
    lista_usuario = input("Agregue una lista de enteros separados por comas")
    lista = list(map(int, lista_usuario.split(',')))
    return lista



def ordenar(lista):
    numero = len(lista)
    for i in range(numero):
        for k in range(0, numero - i - 1):
            if lista[k] > lista[k+1]:
                lista[k], lista[k+1] = lista[k+1], lista[k]
    return lista


# SE CREA LA FUNCION Y SE UTLIZA AQUI
lista = pedir_lista()

lista_ordenada = ordenar(lista)

print('Lista ordenada:', lista_ordenada)