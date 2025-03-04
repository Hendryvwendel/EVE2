from Receptenboek import Receptenboek
from Recept import Recept
from Ingredient import Ingredient
from Stap import Stap
import time

def maak_receptenboek(receptenboek):
    recept1 = Recept("Pasta", "Een heerlijke pasta met spek en room")
    recept2 = Recept("Pasta Pesto", "Een heerlijke pasta met pesto en kip")
    recept3 = Recept("Pasta Bolognese", "Een heerlijke pasta met gehakt en tomatensaus")
    recept4 = Recept("Pizza Margherita", "Een heerlijke pizza met tomatensaus en kaas")
    recept5 = Recept("Pizza Salami", "Een heerlijke pizza met tomatensaus, kaas en salami")
    recept6 = Recept("Pizza Hawaii", "Een heerlijke pizza met tomatensaus, kaas, ham en ananas")
    recept7 = Recept("Sushi", "Een heerlijke sushi met rijst, vis en groente")
    recept8 = Recept("Bami", "Een heerlijke bami met mie, groente en kip")

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
    receptenboek.voeg_recept_toe(recept2)
    receptenboek.voeg_recept_toe(recept3)
    receptenboek.voeg_recept_toe(recept4)
    receptenboek.voeg_recept_toe(recept5)
    receptenboek.voeg_recept_toe(recept6)
    receptenboek.voeg_recept_toe(recept7)
    receptenboek.voeg_recept_toe(recept8)

def voeg_recept_toe(receptenboek):
    print("Voer de naam van het recept in:")
    naam_recept = input()
    print("Voer de beschrijving van het recept in:")
    beschrijving_recept = input()
    recept_toegevoegd = Recept(naam_recept, beschrijving_recept)
    
    while True:
        print("Voer de naam van het ingrediënt in: (typ stop om te stoppen)")
        naam_ingredient = input()
        if naam_ingredient == "stop":
            break
        print("Voer de hoeveelheid in:")
        hoeveelheid = int(input())
        print("Voer de eenheid in:")
        eenheid = input()
        print("Voer het aantal kcal in:")
        kcal = int(input())
        
        ingredient_toegevoegd = Ingredient(naam_ingredient, hoeveelheid, eenheid, kcal)
        recept_toegevoegd.voeg_ingredient_toe(ingredient_toegevoegd)
        
        print("Is voor dit ingredient een plantaardig alternatief? (ja/nee)")
        if input().lower() == "ja":
            print("Voer de naam van het plantaardig alternatief in:")
            naam_ingredient_alternatief = input()
            print("Voer de hoeveelheid in:")
            hoeveelheid_alternatief = int(input())
            print("Voer de eenheid in:")
            eenheid_alternatief = input()
            print("Voer het aantal kcal in:")
            kcal_alternatief = int(input())

            ingredient_toegevoegd_alternatief = Ingredient(naam_ingredient_alternatief, hoeveelheid_alternatief, eenheid_alternatief, kcal_alternatief)
            recept_toegevoegd.voeg_ingredient_toe(ingredient_toegevoegd_alternatief)
    
    while True:
        print("Voer een stap in:")
        beschrijving_stap = input()
        
        print("Wil je een tip toevoegen? (ja/nee)")
        tip = ""
        if input().lower() == "ja":
            print("Voer de tip in:")
            tip = input()
        
        recept_stap = Stap(beschrijving_stap, tip)
        recept_toegevoegd.voeg_stap_toe(recept_stap)
        
        print("Wil je nog een stap toevoegen? (ja/nee)")
        if input().lower() != "ja":
            break
    
    receptenboek.voeg_recept_toe(recept_toegevoegd)
    print(f"Recept '{naam_recept}' toegevoegd!")

def toon_recepten(receptenboek):
    while True:
        print("Dit zijn de recepten die je kan maken:")
        time.sleep(1)
        print(receptenboek.get_recepten_namen())
        gekozen_recept = input("Welk recept wil je maken? ")
        recept = receptenboek.get_recept(gekozen_recept)
        
        if recept == None:
            print("Dit recept bestaat niet.")
            time.sleep(1)
            command = input("Druk op enter om een ander recept te kiezen of typ 'stop' om te stoppen. ")
            if command == "stop":
                break
            else:
                continue
        else:
            time.sleep(1)
            aantal_personen = int(input("Voor hoeveel personen wil je dit recept maken? "))

            recept.set_personen(aantal_personen)

            print(f"Dit is het recept voor {gekozen_recept}:")
            print(recept)
            
            command = input("Wil je dit recept verwijderen? (ja/nee) ")
            if command == "ja":
                receptenboek.verwijder_recept(gekozen_recept)
                print(f"Recept '{gekozen_recept}' verwijderd!")
            else:
                command = input("Druk op enter om een ander recept te kiezen of typ 'stop' om te stoppen. ")
                if command == "stop":
                    break
                else:
                    continue

def main():
    receptenboek = Receptenboek()
    maak_receptenboek(receptenboek)

    # Keuzemenu
    print("Welkom bij het receptenboek!")
    while True:
        print("Kies een optie: toevoegen, tonen, exit")
        keuze = input().lower()
        if keuze == "toevoegen":
            voeg_recept_toe(receptenboek)
        elif keuze == "tonen":
            toon_recepten(receptenboek) 
        elif keuze == "exit":
            break
        else:
            print("Foutieve invoer. Kies toevoegen, tonen of exit.")


if __name__ == "__main__":
    main()