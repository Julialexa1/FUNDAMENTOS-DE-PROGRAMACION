# Crear un nuevo archivo llamado 'my_notes.txt' y escribir en él
with open("my_notes.txt", "w") as file:
    # Escribir tres líneas de notas personales
    file.write("Primera nota: Archivo de lectura.\n")
    file.write("Segunda nota: Para practicar.\n")
    file.write("Tercera nota: Y mejorar en la creacion y lectura de archivos.\n")
    # El archivo se cierra automáticamente al salir del bloque 'with'

# Abrir el archivo 'my_notes.txt' para leerlo
with open("my_notes.txt", "r") as file:
    # Leer el contenido del archivo línea por línea
    linea = file.readline()

    # Imprimir cada línea mientras haya contenido en el archivo
    while linea:
        print(linea.strip())  # 'strip()' elimina cualquier salto de línea adicional
        linea = file.readline()

    # El archivo se cierra automáticamente al salir del bloque 'with'
