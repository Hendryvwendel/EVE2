from spel import Spel

class Winkel:
    def __init__(self, naam: str, capaciteit: int):
        self.__naam = naam
        self.__capaciteit = capaciteit
        self.__spellen = []

    def voeg_spel_toe(self, spel: Spel):
        self.__spellen.append(spel)
        print(f"Spel {spel} toegevoegd aan de winkel")
        print(self.__spellen)

    def geef_langste_spel(self):
        if not self.__spellen:
            return None
        else:
            return max(self.__spellen, key=lambda spel: spel.get_speelduur())

    def __str__(self):
        result = f"--- {self.__naam} --- \nCapaciteit: {self.__capaciteit} spellen \n"
        for spel in self.__spellen:
            result += f"{spel} ({spel.get_categorie()}, {spel.get_speelduur()} minuten)\n"
        return result

