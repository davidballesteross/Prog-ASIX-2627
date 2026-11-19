temps = float(input("Temps fent exercici (hores): "))
litres = int(temps * 0.5)

if temps == 1:
    text_hores = "hora"
else:
    text_hores = "hores"

if litres == 1:
    text_litres = "litre"
else:
    text_litres = "litres"

print("Com has estat", temps, text_hores, "fent exercici, has de beure", litres, text_litres, "de liquid per mantenir-te en un bon nivell d hidratació")
