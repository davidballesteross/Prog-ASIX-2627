import math

preu = float(input("Preu actual del Toblerone: "))

descompte = float(input("% de descompte: "))

despeses = float(input("Despeses de les vacances: "))

benefici_per_unitat = preu * descompte / 100

num_toblerones = math.ceil(despeses / benefici_per_unitat)

print("------------------------------------------------")
print("Preu per unitat:", preu, "€")
print("Descompte per cada unitat:", descompte, "%")
print("Benefici per unitat:", benefici_per_unitat, "€")
print("Despeses de les nostres vacances:", despeses, "€")
print("------------------------------------------------")
print("Nº de Toblerones que hem de comprar i revendre per amortitzar les vacances:", num_toblerones)
print("------------------------------------------------")
