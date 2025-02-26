import Recept

class Receptenboek:
    def __init__(self):
        self.__recepten = []
    
    def voeg_recept_toe(self, recept: Recept):
        self.__recepten.append(recept)
    
    def get_recepten_namen(self):
        namen = "\n".join(recept.get_naam() for recept in self.__recepten)
        return namen
    
    def get_recept(self, naam: str):
        for recept in self.__recepten:
            if recept.get_naam() == naam:
                return recept
            else :
                return None

    def __str__(self):
        recepten = "\n\n".join(str(recept) for recept in self.__recepten)
        return f"Receptenboek:\n{recepten}"