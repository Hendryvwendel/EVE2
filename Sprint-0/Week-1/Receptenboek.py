import Recept

class Receptenboek:
    def __init__(self):
        self.__recepten = []
    
    def voeg_recept_toe(self, recept: Recept):
        self.__recepten.append(recept)
    
    def get_recepten(self):
        return self.__recepten
    
    def __str__(self):
        recepten = "\n\n".join(str(recept) for recept in self.__recepten)
        return f"Receptenboek:\n{recepten}"