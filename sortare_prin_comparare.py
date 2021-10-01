def func(lista, n):
    for i in range(0,n-1):
        min = lista[i]
        pozmin = i
        for j in range(i+1, n):
            if lista[j] < min:
                min = lista[j]
                pozmin = j
        lista[pozmin], lista[i] = lista[i], lista[pozmin]
    return lista
def main():
    lista = [4,1,7,3,-2]
    n = len(lista)
    print(func(lista,n))
main()