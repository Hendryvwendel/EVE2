from Receptenboek import Receptenboek
from Recept import Recept
from Ingredient import Ingredient
from Stap import Stap
from import_recepten import import_recepten
import time

def main():
    import_recepten()

    started = False
    while True:
        if started:
            command = ""
            if command == "":
                print("Welkom bij het receptenboek!")
                started = True
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
                    
                    command = input("Druk op enter om een ander recept te kiezen of typ 'stop' om te stoppen. ")
                    if command == "stop":
                        break
                    else:
                        continue

        else:
            command = input("Druk op enter om te starten")
            if command == "":
                started = True
                continue
        time.sleep(1)
if __name__ == "__main__":
    main()
    