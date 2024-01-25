class Pokemon:

    def __init__(self, name):
        self.__name = name
        # __level - die Variable ist geschützt => um auf die Variable zuzugreifen, muss eine extra Funktion gebaut werden, z.B. zeige_level
        self.__level = 1
        #self.vorstellen()
        self.__lebenspunkte = 42


    # zeigt die Infos vom Pokemon
    def __str__(self):
        return f"Name: {self.__name}\nLeben: {self.__lebenspunkte}\nLevel: {self.__level}"
    

    # prüft, ob das Level von einem Pokemon größer ist als vom anderen und gibt True oder False zurück
    def __gt__(self, other):
        return self.__level > other.__level

    # (self) zeigt, dass die Funktion eine Methode ist
    def zeige_level(self):
        print(f"{self.__name} :: {self.__level}")


    def vorstellen(self):
        print(f"{self.__name}, {self.__name}!") 
        #print(f"Level: {self.zeige_level()}") 


    def zeige_lebenspunkte(self):
        return self.__lebenspunkte
    

    def entwickeln(self):
        self.__level += 1

    
    def attackieren(self, other, schaden):
        other.__lebenspunkte -= schaden



if __name__ == "__main__":
    #bisasam = Pokemon("Bisasam")
    #bisasam.vorstellen()
    #schiggy = Pokemon("Schiggy")
    #schiggy.vorstellen()

    p1 = Pokemon("Pikachu")
    p2 = Pokemon("Bisasam")

    """
    p1.entwickeln()
    p1.entwickeln()
    p1.zeige_level()
    p2.zeige_level()
    """

    #p1.attackieren(p2, 10)
    #print(p2.zeige_lebenspunkte())

    # Methoden brauchen immer ein Objekt, um aufgerufen zu werden 
    p1.entwickeln()
    #p2.attackieren(p1, 5)
    #print(p1)

    print(p1 > p2)
