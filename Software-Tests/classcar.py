class Car:
    def __init__(self, brand: str, model: str, color: str, power: int, doors: int, apk: bool, kenteken: str, kilometerstand: int):

        self.brand = brand
        self.model = model
        self.color = color
        self.power = power
        self.doors = doors
        self.apk = apk
        self.__kilometerstand = kilometerstand
        self.__kenteken = kenteken

    def get_kenteken(self):
        return f"Het kenteken van deze auto is {self.__kenteken}"
    
    def set_kenteken(self, kenteken: str):
        self.__kenteken = kenteken
    
    def get_kilometerstand(self):
        return f"De kilometerstand van deze auto is {self.__kilometerstand}"
    
    def set_kilometerstand(self, kilometerstand: int):
        self.__kilometerstand = kilometerstand

    def __str__(self):
        return f"De kleur van {self.brand} {self.model} is {self.color}. Deze auto heeft {self.power} PK en {self.doors} deuren. {'Deze auto mag niet op de weg omdat er geen geldige APK is' if not self.apk else 'Deze auto mag op de weg'}"
