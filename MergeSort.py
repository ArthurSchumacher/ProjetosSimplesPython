def merge_sort(listaArg, start = 0, end = None):

    if end == None: end = len(listaArg)

    if (end - start > 1):
        middle = (end + start) // 2
        merge_sort(listaArg, start, middle)
        merge_sort(listaArg, middle, end)
        merge(listaArg, start, middle, end)

def merge(listaArg, start, middle, end):
    leftList = listaArg[start:middle]
    rightList = listaArg[middle:end]

    topLeft, topRight = 0, 0

    for i in range(start, end):

        if topLeft >= len(leftList):
            listaArg[i] = rightList[topRight]
            topRight += 1
        
        elif topRight >= len(rightList):
            listaArg[i] = leftList[topLeft]
            topLeft += 1

        elif leftList[topLeft] < rightList[topRight]: 
            listaArg[i] = leftList[topLeft]
            topLeft += 1

        else: 
            listaArg[i] = rightList[topRight]
            topRight += 1

lista = input(f'Digite os números da lista:\n').split()

merge_sort(lista)

print(f'\nLista de números ordenados:')
for index, item in enumerate(lista):
    if index == (len(lista) - 1): print(item)
    if index != (len(lista) - 1): print(item, end=' ')