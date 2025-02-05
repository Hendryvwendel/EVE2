class Spel:
    def __init__(self, naam: str, categorie: str, speelduur: int):
        self.__naam = naam
        self.__categorie = categorie
        self.__speelduur = speelduur

    def get_categorie(self):
        return self.__categorie
    
    def get_speelduur(self):
        return self.__speelduur
    
    def __str__(self):
        return f"{self.__naam} ({self.__categorie}) - {self.__speelduur} minuten"
