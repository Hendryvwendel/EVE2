class Car:
    def __init__(self, brand: str, model: str, color: str, power: int, doors: int, apk: bool):

        self.brand = brand
        self.model = model
        self.color = color
        self.power = power
        self.doors = doors
        self.__apk = apk

    def __str__(self):
        return f"de kleur van {self.brand} {self.model} is {self.color}. Deze auto heeft {self.power} PK en {self.doors} deuren. {'Deze auto mag niet op de weg omdat er geen geldige APK is' if not self.apk else 'Deze auto mag op de weg'}"
