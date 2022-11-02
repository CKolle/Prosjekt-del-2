from enum import Enum
import json
from utils.json.KategoriEncoder import KategoriEncoder


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


class Sted:
    def __init__(self, id: int, navn: str, gateadresse = None, postnummer = None, poststed = None) -> None:
        self.id = id
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.poststed = poststed
    
    def __str__(self) -> str:
        streng_konstruksjon = ''
        egenskap_dict = {'Id': self.id, 'Navn': self.navn, 'Gateadresse': self.gateadresse,
        'Postnummer': self.postnummer, 'Poststed': self.poststed}
        for egenskap, verdi in egenskap_dict.items():
            if verdi:
                streng_konstruksjon+=f'{egenskap}: {verdi}, '
        return streng_konstruksjon.rstrip(', ')


def lag_kategori() -> Kategori:
    """Lager et gyldig kategori objekt"""

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


def lagre_liste(kategorier: list[Kategori]) -> None:
    """Tar inn en liste med kategorier, og lagrer dem i filen kategori.txt på json format"""

    with open("kategori.txt", "w") as kategori_fil:
        json.dump(kategorier, kategori_fil,
                  cls=KategoriEncoder, indent=4, sort_keys=True)


def les_liste() -> list[Kategori]:
    """Leser in en json fil med kategorier. Returnerer en liste med kategorier"""

    with open("kategori.txt", "r") as kateogri_fil:
        kategori_json = json.load(kateogri_fil)

    kategorier = []
    for kategori in kategori_json:
        kategori["prioritet"] = Prioritet(kategori["prioritet"])
        kategori = Kategori(**kategori)
        kategorier.append(kategori)
    return kategorier


def utskrift_kategorier(kategorier: list[Kategori], overskrift=""):
    """Printer en liste med kategorier med indeks, navn og en felles overskrift"""

    if overskrift != "":
        print(overskrift)
    for kategori in kategorier:
        print(f"{kategorier.index(kategori)}: {kategori.navn}")