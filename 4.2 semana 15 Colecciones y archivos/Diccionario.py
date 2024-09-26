# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Jose Luis",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Abogado"
}
print("informacion personal inicial")
print (informacion_personal)

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Cuenca"
print("Nueva ciudad:", informacion_personal["ciudad"])

# Agregar la clave "profesion"
informacion_personal["profesion"] = "Programador"

# Verificar si existe la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0912345678"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal actualizada:")
print(informacion_personal)