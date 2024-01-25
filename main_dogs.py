# Über-Klasse
class Mammal:
    # __init__ ist standartmäßig in jeder class
    def __init__(self, farbe, rasse, name):
        # self.farbe - ist eine Zuweisung an das aktuelle Objekt
        # farbe - ist die Variable aus dem Funktionsparameter

# Eigenschaften
        self.farbe = farbe
        self.rasse = rasse
        self.name = name

    def vorstellen(self):
        print(f"Ich bin {self.name}")

# Methoden   
    def essen(self):
        pass

# (Mammal) vererbt die Eigenschaften von Mammal an Hund
class Hund(Mammal):

    def bellen(self):
        pass

    def laufen(self):
        pass


class Katze(Mammal):
    def miauen(self): 
        print("Miau")

dog1 = Hund('Braun', 'Schäferhund', 'Daisy')
dog2 = Hund('Schwarz', 'Schäferhund', 'Wuffi')

dog1.vorstellen()