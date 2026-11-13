import math

tiempo = float(input("¿Cuántas horas has estado haciendo ejercicio? "))

litros_necesarios = tiempo * 0.5

botellas = math.floor(litros_necesarios)

print("Com has estat", tiempo, "hores fent exercici, has de beure", botellas, "litre de líquid per mantenir-te en un bon nivell d hidratació")
