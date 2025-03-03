#crear una matriz bidemensional 3x3 con valores numericos
#implementar funcion de busqueda para encontrar un valor especifico definido

"Bienvenido al programa los primeros nueve numeros impares"
"intenta inserter alguno de los primero nueves"

lista_impares = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17],
]


valor_buscado = 11
fila_encontrada = 3
columna_encontrada = 3 

for fila in range (len(lista_impares)):
    for columna in range(len(lista_impares[fila])):
        if lista_impares[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna 
            break
        if fila_encontrada != 3:
            print("Se encontro (valor_buscado) en la fila (fila_encontrada) y columna (columna encontrada)")

        else:
            print("No se encontro (valor_buscado) en la lista_impares")


