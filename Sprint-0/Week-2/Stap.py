class Stap:
    def __init__(self, beschrijving: str):
        self.__beschrijving = beschrijving
    
    def __str__(self):
        return (f"{self.__beschrijving}")