class PoraRoku:
    def __init__(self, nazwa, temperatura, opis, typowe_zjawiska):
        self.nazwa = nazwa
        self.temperatura = temperatura
        self.opis = opis
        self.typowe_zjawiska = typowe_zjawiska

    def __str__(self):
        return (f"Pora roku: {self.nazwa}"
                f"Temperatura: {self.temperatura}"
                f"Opis: {self.opis}"
                f"Typowe zjawiska: {', '.join(self.typowe_zjawiska)}")
