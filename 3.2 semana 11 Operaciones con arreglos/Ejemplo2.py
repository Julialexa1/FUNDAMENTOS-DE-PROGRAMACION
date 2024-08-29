# Ordenación de Arreglo Multidimensional
# Matriz de 3x3

matriz = [
    [5, 7, 15],
    [9, 12, 4],
    [3, 17, 8]
]

print(matriz)
#metodo de ordenamiento bubble_sort
def bubble_sort(fila):
    #algoritmo bubble Sort
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i,-1):
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)
print("matriz original")
print(matriz)
bubble_sort(matriz[2])
print(matriz)
