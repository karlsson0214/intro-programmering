def min(lista):
    minsta = lista[0]
    for tal in lista:
        if tal < minsta:
            minsta = tal
    return minsta


mina_tal = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(min(mina_tal))



