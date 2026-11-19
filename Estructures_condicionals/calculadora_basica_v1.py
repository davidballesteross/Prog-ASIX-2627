operacio = input("Introdueix operació a realitzar (+,-,*,/): ")
num1 = float(input("Introdueix el primer nº: "))
num2 = float(input("Introdueix el segon nº: "))

print("----------------------------------------------")

if operacio == "+":
    resultat = num1 + num2
    print(num1, "+", num2, "=", resultat)
elif operacio == "-":
    resultat = num1 - num2
    print(num1, "-", num2, "=", resultat)
elif operacio == "*":
    resultat = num1 * num2
    print(num1, "*", num2, "=", resultat)
elif operacio == "/":
    if num2 == 0:
        print("Error: No es pot dividir per zero")
    else:
        resultat = num1 / num2
        print(num1, "/", num2, "=", resultat)
else:
    print("Error: Operació no vàlida")

print("----------------------------------------------")
