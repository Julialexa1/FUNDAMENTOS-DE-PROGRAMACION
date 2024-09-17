# Definir la función para calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
def main():
    # Primera llamada: solo proporcionar el monto total de la compra
    monto1 = 1200
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Compra de ${monto1}: Descuento de ${descuento1:.2f}, Monto final a pagar: ${monto_final1:.2f}")

    # Segunda llamada: proporcionar tanto el monto total como el porcentaje de descuento
    monto2 = 700
    porcentaje_descuento2 = 20
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
    monto_final2 = monto2 - descuento2
    print(
        f"Compra de ${monto2} con {porcentaje_descuento2}% de descuento: Descuento de ${descuento2:.2f}, Monto final a pagar: ${monto_final2:.2f}")


# Ejecutar el programa principal
main()
