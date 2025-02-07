from winkel import Winkel
import spel
def main():
    winkel = Winkel("Speeleiland", 4)

    spel1 = spel("Catan", "strategie", 120)
    spel2 = spel("Monopoly", "bordspel", 90)
    spel3 = spel("Uno", "kaartspel", 30)
    spel4 = spel("Wingspan", "strategie", 40)
    spel5 = spel("Ganzenbord", "bordspel", 30)

    print(spel1)  # Catan (strategie, 120 minuten)

    winkel.voeg_spel_toe(spel1)
    winkel.voeg_spel_toe(spel2)
    winkel.voeg_spel_toe(spel3)
    winkel.voeg_spel_toe(spel4)
    winkel.voeg_spel_toe(spel5)  # De winkel is vol

    print(winkel)  
    # --- Speeleiland ---
    # Capaciteit: 4 spellen
    # Catan (strategie, 120 minuten)
    # Monopoly (bordspel, 90 minuten)
    # Uno (kaartspel, 30 minuten)
    # Wingspan (strategie, 40 minuten)


if __name__ == "__main__":
    main()