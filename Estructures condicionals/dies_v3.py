print("------------------------------------------")
civilitzacio = input("Es vosté Interiá (I) o Stringeriá (S)?: ")
print("------------------------------------------")

if civilitzacio == "I":
    dia = input("Día de la setmana: ")
    if dia == "Dilluns":
        print("Traducció: 1")
    elif dia == "Dimarts":
        print("Traducció: 2")
    elif dia == "Dimecres":
        print("Traducció: 3")
    elif dia == "Dijous":
        print("Traducció: 4")
    elif dia == "Divendres":
        print("Traducció: 5")
    elif dia == "Dissabte":
        print("Traducció: 6")
    elif dia == "Diumenge":
        print("Traducció: 7")
    else:
        print("Error: Dia no vàlid")

elif civilitzacio == "S":
    dia = int(input("Día de la setmana: "))
    if dia == 1:
        print("Traducció: Dilluns")
    elif dia == 2:
        print("Traducció: Dimarts")
    elif dia == 3:
        print("Traducció: Dimecres")
    elif dia == 4:
        print("Traducció: Dijous")
    elif dia == 5:
        print("Traducció: Divendres")
    elif dia == 6:
        print("Traducció: Dissabte")
    elif dia == 7:
        print("Traducció: Diumenge")
    else:
        print("Error: Dia no vàlid")

else:
    print("Error: Civilització no reconeguda")

print("------------------------------------------")
