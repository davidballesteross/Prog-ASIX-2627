stock = int(input("Stock inicial de pocions: "))

c1 = int(input("Compra client 1: "))
c2 = int(input("Compra client 2: "))
c3 = int(input("Compra client 3: "))

stock_final = stock - c1 - c2 - c3

print("Stock inicial:", stock)
print("------------------------")
print("Compra client 1: -" + str(c1))
print("Compra client 2: -" + str(c2))
print("Compra client 3: -" + str(c3))
print("------------------------")
print("Stock al final del dia:", stock_final, "pocions")
