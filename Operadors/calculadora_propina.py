importe = float(input("Importe de la cuenta: "))

porcentaje = float(input("Porcentaje de propina: "))

propina = importe * porcentaje / 100

total = importe + propina

print("Importe inicial:", importe, "€")
print("Propina (" + str(porcentaje) + "%):", propina, "€")
print("---------------------")
print("Total a pagar:", total, "€")
