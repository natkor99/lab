class PoraRoku:
    def __init__(self, nazwa, temperatura, opis, typowe_zjawiska):
        self.nazwa = nazwa
        self.temperatura = temperatura
        self.opis = opis
        self.typowe_zjawiska = typowe_zjawiska

    def __str__(self):
        return (f"Pora roku: {self.nazwa}\n"
                f"Temperatura: {self.temperatura}\n"
                f"Opis: {self.opis}\n"
                f"Typowe zjawiska: {', '.join(self.typowe_zjawiska)}")

wiosna = PoraRoku(
    nazwa="Wiosna",
    temperatura="umiarkowana",
    opis="Czas, kiedy przyroda budzi się do życia, kwitną kwiaty.",
    typowe_zjawiska=["kwitnienie drzew", "częste deszcze", "cieplejsze dni"]
)

lato = PoraRoku(
    nazwa="Lato",
    temperatura="ciepła",
    opis="Najgorętsza pora roku z długimi, słonecznymi dniami.",
    typowe_zjawiska=["upały", "burze"]
)

jesien = PoraRoku(
    nazwa="Jesień",
    temperatura="chłodna",
    opis="Okres opadania liści i coraz chłodniejszych dni.",
    typowe_zjawiska=["opadające liście", "chłodne wieczory", "deszcz"]
)

zima = PoraRoku(
    nazwa="Zima",
    temperatura="zimna",
    opis="Najzimniejsza pora roku, często z opadami śniegu.",
    typowe_zjawiska=["śnieg", "mróz", "krótkie dni"]
)

print(wiosna)
print()
print(lato)
print()
print(jesien)
print()
print(zima)

