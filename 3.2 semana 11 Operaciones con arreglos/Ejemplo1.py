#Búsqueda en Arreglo Multidimensional
# Matriz de 3x3

matriz = [
    [2, 5, 9],
    [8, 3, 1],
    [6, 7, 4]
]

print(matriz)

# Funcion para buscar un valor especifico en la matriz

def buscar_valor(matriz,valor_especifico):
 for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] == valor_especifico:
            return i,j

valor_especifico = 1
#print(buscar_valor(matriz,valor_especifico))

if valor_especifico == valor_especifico:
    print("Valor encontrado en la posicion",buscar_valor(matriz,valor_especifico))
else:
    print("Valor inexistente")

