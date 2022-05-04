# Widmark-Formel Programm
# von Judith und Rosalie 

#Überschrift
print("Dieses Programm berechnet den Blutalkoholwert in Promille")

#Variablen eingeben
körpergewichttext: str = input("Ihr Körpergewicht in Kilogramm: ")
anzahlflaschentext: str = input("Wie viele Flaschen Bier haben sie getrunken?: ")
geschlecht: str = input("Sind sie männlich (m) oder weiblich (w): ")

#texteingaben in Zahlen umwandeln
körpergewicht: float =float(körpergewichttext)
anzahlflaschen: float =float(anzahlflaschentext)

#alkoholmasse berechnen
alkoholmasse: float= anzahlflaschen*0.5*0.5*0.8*100
print("Alkoholmasse= ",alkoholmasse ," Gramm")

#Reduktionsfaktor bestimmen
reduktionsfaktor: float=0
if geschlecht == "m":
    reduktionsfaktor=0.7
else:
    reduktionsfaktor=0.6
print("geschlecht: ",geschlecht,", das bedeutet einen Reduktionsfaktor von: ", reduktionsfaktor)

#Blutalkohol
blutalkoholinpromille: float = alkoholmasse/(körpergewicht*reduktionsfaktor)
print("Ihr Blutalkoholwert in Promille beträgt: ", round(blutalkoholinpromille, 2))
