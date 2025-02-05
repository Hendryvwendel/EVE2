from winkel import Winkel
from spel import Spel

def main():
    winkel = Winkel("Speeleiland", 4)

    spel1 = Spel("Catan", "strategie", 120)
    spel2 = Spel("Monopoly", "bordspel", 90)
    spel3 = Spel("Uno", "kaartspel", 30)
    spel4 = Spel("Wingspan", "strategie", 40)
    spel5 = Spel("Ganzenbord", "bordspel", 30)

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