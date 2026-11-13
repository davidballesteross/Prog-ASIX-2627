stock_inicial = int(input("Stock inicial de pociones: "))

stock_actual = stock_inicial

compra1 = int(input("¿Cuántas pociones compra el cliente 1? "))
stock_actual = stock_actual - compra1
print("Quedan:", stock_actual, "pociones")

compra2 = int(input("¿Cuántas pociones compra el cliente 2? "))
stock_actual = stock_actual - compra2
print("Quedan:", stock_actual, "pociones")

compra3 = int(input("¿Cuántas pociones compra el cliente 3? "))
stock_actual = stock_actual - compra3
print("Quedan:", stock_actual, "pociones")

print("------------------------")
print("Stock inicial:", stock_inicial)
print("------------------------")
print("Compra client 1: -" + str(compra1))
print("Compra client 2: -" + str(compra2))
print("Compra client 3: -" + str(compra3))
print("------------------------")
print("Stock al final del dia:", stock_actual, "pociones")
