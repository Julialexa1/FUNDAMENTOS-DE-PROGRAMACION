# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (2 ciudades)
# Segunda dimensión: Semanas (2 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [  # Ciudad 1
        [20, 22, 21, 23, 19, 20, 24],  # Semana 1
        [25, 26, 24, 22, 21, 23, 24]  # Semana 2
    ],
    [  # Ciudad 2
        [18, 19, 20, 21, 22, 19, 20],  # Semana 1
        [22, 24, 23, 21, 22, 23, 25]  # Semana 2
    ]
]

# Nombres de las ciudades y semanas
ciudades = ['Ciudad 1', 'Ciudad 2']
semanas = ['Semana 1', 'Semana 2']

# Calcular el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(temperaturas):
    print(f"\nPromedios de temperatura para {ciudades[i]}:")

    for j, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)  # Calcular el promedio
        print(f"  {semanas[j]}: {promedio:.2f}°C")  # Mostrar el promedio