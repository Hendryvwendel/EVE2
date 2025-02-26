import Ingredient
class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str, kcal: int, personen: int = 1):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__personen = personen
        self.__eenheid = eenheid
        self.__kcal = kcal
        self.__plantaardig_alternatief = None

        self.__hoeveelheid = self.__hoeveelheid * self.__personen
        self.__kcal = self.__kcal * self.__personen

    def set_hoeveelheid(self, hoeveelheid: float):
        self.__hoeveelheid = hoeveelheid

    def get_hoeveelheid(self):
        return self.__hoeveelheid
    
    def get_kcal(self):
        return self.__kcal
    
    def set_personen(self, personen: int):
        self.__personen = personen
        self.__hoeveelheid = self.__hoeveelheid * self.__personen
        self.__kcal = self.__kcal * self.__personen

    def set_plantaardig_alternatief(self, plantaardig_alternatief: Ingredient):
        self.__plantaardig_alternatief = plantaardig_alternatief
    
    def get_plantaardig_alternatief(self):
        return self.__plantaardig_alternatief

    def get_ingredient(self, plantaardig: bool = False):
        if plantaardig == True:
            return self.__plantaardig_alternatief
        else:
            return self

    def __str__(self):
        return (f"{self.__hoeveelheid} {self.__eenheid} {self.__naam}." + 
        (f" Het plantaardig alternatief is {self.__plantaardig_alternatief}" if self.__plantaardig_alternatief else ""))