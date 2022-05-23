def bubble_sort(listaArg):

    for i in range(len(listaArg) - 1):
        for j in range(len(listaArg) - 1):
            if listaArg[j] > listaArg[j + 1]:
                listaArg[j], listaArg[j + 1] = listaArg[j + 1], listaArg[j]
    
    return listaArg

lista = input(f'Digite os números da lista:\n').split()

bubble_sort(lista)

print(f'\nLista de números ordenados:')
for index, item in enumerate(lista):
    if index == (len(lista) - 1): print(item)
    if index != (len(lista) - 1): print(item, end=' ')