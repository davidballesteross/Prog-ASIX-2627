operacio = input("Introdueix operació a realitzar (+,-,*,/): ")

if operacio != "+" and operacio != "-" and operacio != "*" and operacio != "/":
    print("Error: Operació no vàlida")
else:
    try:
        num1 = float(input("Introdueix el primer nº: "))
    except ValueError:
        print("Error: El primer valor no és un número")
        exit()

    try:
        num2 = float(input("Introdueix el segon nº: "))
    except ValueError:
        print("Error: El segon valor no és un número")
        exit()

    print("----------------------------------------------")
    if operacio == "+":
        print(num1, "+", num2, "=", num1 + num2)
    elif operacio == "-":
        print(num1, "-", num2, "=", num1 - num2)
    elif operacio == "*":
        print(num1, "*", num2, "=", num1 * num2)
    elif operacio == "/":
        if num2 == 0:
            print("Error: No es pot dividir per zero")
        else:
            print(num1, "/", num2, "=", num1 / num2)
    print("----------------------------------------------")
