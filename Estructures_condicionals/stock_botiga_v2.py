stock = int(input("Stock inicial de pocions: "))
stock_inicial = stock
c1 = 0
c2 = 0
c3 = 0

# Client 1
if stock > 0:
    c1 = int(input("Compra client 1: "))
    if c1 > stock:
        print("Només li puc vendre", stock, "unitats")
        c1 = stock
    stock = stock - c1
    if stock == 0:
        print("Pocions exhaurides. Torni demà")

# Client 2
if stock > 0:
    c2 = int(input("Compra client 2: "))
    if c2 > stock:
        print("Només li puc vendre", stock, "unitats")
        c2 = stock
    stock = stock - c2
    if stock == 0:
        print("Pocions exhaurides. Torni demà")

# Client 3
if stock > 0:
    c3 = int(input("Compra client 3: "))
    if c3 > stock:
        print("Només li puc vendre", stock, "unitats")
        c3 = stock
    stock = stock - c3
    if stock == 0:
        print("Pocions exhaurides. Torni demà")

print("Stock inicial:", stock_inicial)
print("------------------------")
print("Compra client 1: -" + str(c1))
print("Compra client 2: -" + str(c2))
print("Compra client 3: -" + str(c3))
print("------------------------")
print("Stock al final del dia:", stock, "pocions")
