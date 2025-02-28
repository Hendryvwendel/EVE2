from Receptenboek import Receptenboek
from Recept import Recept
from Ingredient import Ingredient
from Stap import Stap
import time

def main():
    receptenboek = Receptenboek()

    recept1 = Recept("Pasta Carbonara", "Een heerlijke pasta met spek en room")

    ingredient1 = Ingredient("Pasta", 200, "gram", 400)
    ingredient2 = Ingredient("Spek", 100, "gram", 200)
    ingredient3 = Ingredient("Eieren", 2, "stuks", 150)
    ingredient4 = Ingredient("Room", 100, "ml", 200)
    ingredient5 = Ingredient("Kaas", 50, "gram", 100)

    ingredient2.set_plantaardig_alternatief(Ingredient("Tofu", 100, "gram", 150))
    ingredient4.set_plantaardig_alternatief(Ingredient("Sojaroom", 100, "ml", 200))
    ingredient5.set_plantaardig_alternatief(Ingredient("Vegan kaas", 50, "gram", 100))

    recept1.voeg_ingredient_toe(ingredient1)
    recept1.voeg_ingredient_toe(ingredient2)
    recept1.voeg_ingredient_toe(ingredient3)
    recept1.voeg_ingredient_toe(ingredient4)
    recept1.voeg_ingredient_toe(ingredient5)

    recept1.voeg_ingredient_toe(ingredient1)
    recept1.voeg_ingredient_toe(ingredient2)
    recept1.voeg_ingredient_toe(ingredient3)
    recept1.voeg_ingredient_toe(ingredient4)
    recept1.voeg_ingredient_toe(ingredient5)

    stap1 = Stap("Kook de pasta")
    stap1.voeg_tip_toe("Voeg zout toe aan het water")

    stap2 = Stap("Bak de spek")
    stap2.voeg_tip_toe("Bak de spek krokant")

    stap3 = Stap("Klop de eieren")

    stap4 = Stap("Voeg room toe")
    stap4.voeg_tip_toe("Voeg peper toe")

    stap5 = Stap("Voeg kaas toe")

    recept1.voeg_stap_toe(stap1)
    recept1.voeg_stap_toe(stap2)
    recept1.voeg_stap_toe(stap3)
    recept1.voeg_stap_toe(stap4)
    recept1.voeg_stap_toe(stap5)

    receptenboek.voeg_recept_toe(recept1)


    
    print("Welkom bij het receptenboek!")
    while True:
        command = input("Wat wil je doen? (overzicht tonen, toevoegen, stoppen): ")
        if command == "stoppen":
            break
        elif command == "overzicht tonen":
            print(receptenboek.get_recepten_namen())
            time.sleep(1)
            command = input("Welk recept wil je zien? (typ stop om te terug te gaan): ")
            if command == "stop":
                continue
            aantal_personen = int(input("Voor hoeveel personen wil je dit recept maken? "))
            recept = receptenboek.get_recept(command)
            recept.set_personen(aantal_personen)
            print(recept)
            time.sleep(1)
        elif command == "toevoegen":
            naam_recept = input("Wat is de naam van het recept? ")
            beschrijving_recept = input("Wat is de beschrijving van het recept? ")
            recept_toegevoegd = Recept(naam_recept, beschrijving_recept)
            receptenboek.voeg_recept_toe(recept_toegevoegd)
            stap = input("Wil je een stap toevoegen? (ja/nee): ")
            while stap == "ja":
                beschrijving_stap = input("Wat is de beschrijving van de stap? ")
                tip = input("Heb je een tip voor deze stap? (ja/nee): ")
                if tip == "ja":
                    tip = input("Wat is de tip? ")
                else:
                    tip = None
                recept_stap = Stap(beschrijving_stap, tip)
                recept_toegevoegd.voeg_stap_toe(recept_stap)

                print(recept_toegevoegd.get_stappen())

                stap = input("Wil je nog een stap toevoegen? (ja/nee): ")
            ingredient = input("Wil je een ingredient toevoegen? (ja/nee): ")
            while ingredient == "ja":
                print("De hoeveelheden moeten voor 1 persoon zijn!")
                naam_ingredient = input("Wat is de naam van het ingredient? ")
                hoeveelheid = input("Hoeveel heb je nodig? ")
                eenheid = input("Wat is de eenheid? ")
                kcal = input("Hoeveel kcal bevat het ingredient? ")
                ingredient_toegevoegd = Ingredient(naam_ingredient, hoeveelheid, eenheid, kcal)
                recept_toegevoegd.voeg_ingredient_toe(ingredient_toegevoegd)
                print(recept_toegevoegd)
                ingredient = input("Wil je nog een ingredient toevoegen? (ja/nee): ")
            time.sleep(1)


if __name__ == "__main__":
    main()