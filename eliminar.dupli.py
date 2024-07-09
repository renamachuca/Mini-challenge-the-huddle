def eliminar_duplicados(lista):
    elementos_unicos =  set()
    resultado = []

    for elemento in lista:
        if elemento not in elementos_unicos:
            elementos_unicos.add(elemento)
            resultado.append(elemento)

    return resultado

if __name__ == "__main__":
    lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
    lista_sin_duplicados = eliminar_duplicados(lista)
    print(f'Lista original: {lista}')
    print(f'Lista sin duplicados: {lista_sin_duplicados}')