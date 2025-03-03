"Bienvenido al programa ordenando los enteros"

lista = [5, 7, 3, 1, 8, 4, 9, 2, 6]

for i in range(len(lista) - 1):
    for j in range (len(lista) - 1):
        if lista[j] > lista [j+1]:

            temporal = lista [j]
            lista[j] = lista [j+1]
            lista[j+1] = temporal

print(lista)



