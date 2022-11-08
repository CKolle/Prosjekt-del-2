from enum import Enum
import json
from utils.json.KategoriEncoder import KategoriEncoder
from utils.input_hjelper import hent_int


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
    """Lager et gyldig kategori objekt"""

    navn = input("Skriv inn et navn på kategorien: ")

    id = hent_int("Skriv inn en id: ",
                  "Ugyldig ID, prøv igjen. Husk id er et tall")

    prioritet_valg = hent_int(
        "Velg en prioritet\n Vanlig [1]\n Viktig [2]\n Svært vikitg [3]\n: ", "Ugyldig valg", 1, 3)

    prioritet = Prioritet(prioritet_valg)
    return Kategori(id, navn, prioritet)


def lagre_avtaler(kategorier: list[Kategori]) -> None:
    """Tar inn en liste med kategorier, og lagrer dem i filen kategori.txt på json format"""

    with open("kategori.txt", "w") as kategori_fil:
        json.dump(kategorier, kategori_fil,
                  cls=KategoriEncoder, indent=4, sort_keys=True)


def les_kategorier() -> list[Kategori]:
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
