def insertion_sort(listaArg):

    for i in range(1, len(listaArg)):
        key = listaArg[i]
        j = i - 1
        
        while j >= 0 and listaArg[j] > key:
            listaArg[j + 1] = listaArg[j]
            j -= 1
        
        listaArg[j + 1] = key

lista = input(f'Digite os números da lista:\n').split()

insertion_sort(lista)

print(f'\nLista de números ordenados:')
for index, item in enumerate(lista):
    if index == (len(lista) - 1): print(item)
    if index != (len(lista) - 1): print(item, end=' ')