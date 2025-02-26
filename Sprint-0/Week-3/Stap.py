class Stap:
    def __init__(self, beschrijving: str, tip: str = None):
        self.__beschrijving = beschrijving
        self.__stapnummer = None
        self.__tip = tip

    def voeg_tip_toe(self, tip: str):
        self.__tip = tip

    def set_nummer(self, nummer: int):
        self.__stapnummer = nummer

    def __str__(self):
        if self.__tip is not None:
            return f" {self.__stapnummer}. {self.__beschrijving}, (Tip! {self.__tip})"
        else:
            return f" {self.__stapnummer}. {self.__beschrijving}"