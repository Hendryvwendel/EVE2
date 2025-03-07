from Receptenboek import Receptenboek
from Recept import Recept
from Ingredient import Ingredient
from Stap import Stap

def main():
    receptenboek = Receptenboek()

    recept1 = Recept("Pasta", "1 portie pasta")
    recept2 = Recept("Pizza Salami", "Pizza met salami")

    recept1.voeg_ingredient_toe(Ingredient("Pasta", "200", "gram"))
    recept1.voeg_ingredient_toe(Ingredient("Tomaten", "2", "stuks"))
    recept1.voeg_stap_toe(Stap("Kook de pasta"))
    recept1.voeg_stap_toe(Stap("Snij de tomaten"))

    recept2.voeg_ingredient_toe(Ingredient("Pizza", "1", "stuks"))
    recept2.voeg_ingredient_toe(Ingredient("Salami", "100", "gram"))
    recept2.voeg_stap_toe(Stap("Verwarm de oven"))
    recept2.voeg_stap_toe(Stap("Leg de pizza in de oven"))

    receptenboek.voeg_recept_toe(recept1)
    receptenboek.voeg_recept_toe(recept2)

    print(receptenboek)

if __name__ == "__main__":
    main()
    