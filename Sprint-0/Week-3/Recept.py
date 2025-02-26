import Ingredient
import Stap

class Recept:
    def __init__(self, naam: str, omschrijving: str, personen: int = 1):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__aantal_personen = personen
        self.__ingredient_list = []
        self.__stappen_list = []
    
    def voeg_ingredient_toe(self, ingredient: Ingredient):
        self.__ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap: Stap):
        self.__stappen_list.append(stap)
    
    def get_naam(self):
        return self.__naam
    
    def get_personen(self):
        return self.__aantal_personen
    
    def set_personen(self, personen: int):
        self.__aantal_personen = personen
        for ingredient in self.__ingredient_list:
            ingredient.set_personen(personen)
    
    def __str__(self):
        ingredienten = "\n".join(str(ingredient) for ingredient in self.__ingredient_list)

        totale_kcal = 0
        for ingredient in self.__ingredient_list:
            totale_kcal += ingredient.get_kcal()

        kcal_per_persoon = totale_kcal / self.__aantal_personen

        stapnummer = 1
        for stap in self.__stappen_list:
            stap.set_nummer(stapnummer)
            stapnummer += 1    

        stappen = "\n".join(str(stap) for stap in self.__stappen_list)
        return (f"\n{self.__naam}: {self.__omschrijving}. \n\nDit recept heeft een waarde van {kcal_per_persoon} kcal per persoon ({totale_kcal} kcal in totaal). \n\nIngredienten:\n{ingredienten} \n\nStappen:\n{stappen}")
        