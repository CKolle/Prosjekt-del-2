from enum import Enum


class Prioritet(Enum):
    VANLIG = 1
    VIKTIG = 2
    SVAERT_VIKTIG = 3


class Kategori:
    def __init__(self, id: int, navn: str, prioritet: Prioritet) -> None:
        self.id = id
        self.navn = navn
        self.prioritet = prioritet

    def __str__(self) -> str:
        return f"Id: {self.id}, Navn: {self.navn}, Prioritet: {self.prioritet.name.lower().replace('ae', 'æ').replace('_', ' ')}"


def lag_kategori() -> Kategori:
    navn = input("Skriv inn et navn på kategorien: ")
    while True:
        id = input("Skriv inn en id: ")
        try:
            id = int(id)
        except ValueError:
            print("Ugyldig ID, prøv igjen. Husk id er et tall")
            continue
        break
    while True:
        print("Velg en prioritet")
        print("Vanlig [1]")
        print("Viktig [2]")
        print("Svært viktig [3]")
        valg = input(": ")
        try:
            valg = int(valg)
            prioritet = Prioritet(valg)
        except ValueError:
            print("Ugyldig valg, prøv igjen")
            input("Trykk en knapp for å prøve igjen...")
            continue
        break
    return Kategori(id, navn, prioritet)
