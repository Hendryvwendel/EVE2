from Receptenboek import Receptenboek
from Recept import Recept
from Stap import Stap
from Ingredient import Ingredient



def import_recepten():
    receptenboek = Receptenboek()
    
    recept1 = Recept("Pasta Carbonara", "Een heerlijke pasta met spek en room")
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