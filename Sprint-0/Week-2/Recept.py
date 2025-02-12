import Ingredient
import Stap

class Recept:
    def __init__(self, naam: str, omschrijving: str):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen_list = []
    
    def voeg_ingredient_toe(self, ingredient: Ingredient):
        self.__ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap: Stap):
        self.__stappen_list.append(stap)
    
    def get_naam(self):
        return self.__naam
    
    def __str__(self):
        ingredienten = "\n".join(str(ingredient) for ingredient in self.__ingredient_list)
        stappen = "\n".join(str(stap) for stap in self.__stappen_list)
        return (f"\n{self.__naam}: {self.__omschrijving}. \nIngredienten:\n{ingredienten}. \n\nStappen:\n{stappen}")
        