from medewerker import Medewerker

def main():
    medewerker = Medewerker("Hassan", 2500)
    medewerker.set_salaris(-10) # Salaris mag niet onder 0 komen
    print(medewerker.get_salaris()) # 2500
    medewerker.set_salaris(2750)
    print(medewerker.get_salaris()) # 2750
    medewerker.set_email("hassan@test.nl")
    print(medewerker.get_email()) # hassan@test.nl
    medewerker.set_email("hassan1@test.nl") # E-mailadres mag niet worden gewijzigd
    print(medewerker.get_email()) # hassan@test.nl
    medewerker1 = Medewerker("Evert", 1950, "evert@test.nl")
    medewerker1.set_email("evert1@test.nl") # E-mailadres mag niet worden gewijzigd
    print(medewerker1.get_email())# evert@test.nl 

if __name__ == "__main__":
    main()