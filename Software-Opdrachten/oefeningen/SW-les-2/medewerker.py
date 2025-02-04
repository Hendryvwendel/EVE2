class Medewerker:
    def __init__(self, naam: str, salaris: int, email: str = "???"):
        self.__naam = naam
        self.__salaris = salaris
        self.__email = email

    def set_salaris(self, salaris: int):
        if salaris > 0:
            self.__salaris = salaris
        elif salaris < 0:
            print("Salaris kan niet negatief zijn")

    def get_salaris(self):
        return self.__salaris

    def get_email(self):
        return self.__email
    
    def set_email(self, email: str):
        if self.__email == "???":
            self.__email = email
        else:
            print("E-mailadres mag niet worden gewijzigd")