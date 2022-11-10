from datetime import datetime
from utils.input_hjelper import hent_int, hent_datoklokkeslett
import json
from utils.json.AvtaleEncoder import AvtaleEncoder
from modeller.kategori import *
from modeller.sted import *


class Avtale:
    def __init__(self, tittel: str, sted: Sted, varighet_min: int, starttidspunkt: datetime, kategorier: list[Kategori] = None) -> None:
        self.tittel = tittel
        self.sted = sted
        self.varighet_min = varighet_min
        self.starttidspunkt = starttidspunkt
        self.kategorier = kategorier

    def __str__(self):
        return f"Avtale: {self.tittel}\nSted: {self.sted}\nVarighet: {self.varighet_min} min\nDato: {self.starttidspunkt.strftime('%d.%m.%Y kl. %H:%M')}"
    
    def legg_til_kategori(self, kategori: Kategori) -> None:
        if self.kategorier:
            self.kategorier.append(kategori)
        else:
            self.kategorier = [kategori]


def lag_avtale() -> Avtale:
    """Lager et gyldig avtale objekt"""

    tittel = input("Vennligst oppgi navnet på tittelen på avtalen: ")
    sted = input("Vennligst oppgi stedet for avtalen: ")
    varighet_min = hent_int(
        "Vengligst oppgi hvor lenge avtalen varer (minutter): ", "Ugyldig tall, prøv igjen", 1)
    starttidspunkt = hent_datoklokkeslett()
    return Avtale(tittel, sted, varighet_min, starttidspunkt)


def utskrift_avtaler(avtaler: list[Avtale], overskrift: str = None):
    """Printer en liste med avtaler med indeks tittel og en felles overskrift"""

    if overskrift:
        print(overskrift)
    for avtale in avtaler:
        print(f"{avtaler.index(avtale)}: {avtale.tittel}")


def lagre_avtaler(avtaler: list[Avtale], kategorier: list[Kategori] = None, steder: list[Sted] = None):
    """Lagrer ei liste med avtaler, filer og steder til filer"""
    if kategorier:
        lagre_kategorier(kategorier)
    if steder:
        lagre_sted(steder)
    with open("avtale.txt", "w") as avtale_fil:
        json.dump(avtaler, avtale_fil, indent=4,
                  cls=AvtaleEncoder, sort_keys=True)


def les_avtaler(filnavn_avtaler: str, filnavn_kategorier: str = None, filnavn_steder: str = None):
    """Leser inn avtaler, kategorier og steder fra filer"""

    if filnavn_kategorier:
        kategorier_liste = les_kategorier(filnavn_kategorier)
    else:
        kategorier_liste = None

    if filnavn_steder:
        stedliste = les_sted(filnavn_steder)
    else:
        stedliste = None

    with open(filnavn_avtaler, "r") as avtale_fil:
        avtaler_json = json.load(avtale_fil)

    # Konverterer fra tekst til en liste med avtale objekter
    avtaler_liste = []
    for avtale in avtaler_json:
        avtale['starttidspunkt'] = datetime.fromisoformat(
            avtale['starttidspunkt'])
        avtale = Avtale(**avtale)
        avtaler_liste.append(avtale)
    
    return {'kategorier': kategorier_liste, 'stedliste': stedliste, 'avtaler': avtaler_liste}


def datofiltrer_avtale(avtale_liste: list[Avtale], dato: datetime):
    """Velger dato, henter avtaler på denne datoen"""

    filtrert = filter(lambda avtale: (
        avtale.starttidspunkt.date() == dato), avtale_liste)
    return list(filtrert)


def strengfiltrer_avtale(avtale_liste: list[Avtale], streng: str):
    """Søker strenger i en avtale"""

    filtrert = filter(lambda avtale: (avtale.tittel in streng), avtale_liste)
    return list(filtrert)


def slett_avtale(avtale_lister):
    """Spør brukeren om en avtale og sletter den"""

    max = len(avtale_lister) - 1
    min = 0
    key = hent_int("Hvilken avtale vil du slette: ",
                   "Oppgi en gyldig avtale", min, max, utskrift_avtaler, avtale_lister)
    del avtale_lister[key]


def endre_avtale(avtale_lister: list[Avtale]):
    """Spør brukeren om en avtale og lagter en ny avtale"""

    max = len(avtale_lister) - 1
    min = 0
    key = hent_int(f"Hvilken avtale vil du endre: ",
                   "Oppgi en gyldig avtale", min, max, utskrift_avtaler, avtale_lister)
    del avtale_lister[key]
    ny_avtale = lag_avtale()
    avtale_lister.append(ny_avtale)
    return avtale_lister


def vis_avtale(avtale_lister: list[Avtale]):
    """Spør brukeren om en avtale og viser den"""

    if not avtale_lister:
        print("Du har ingen avtaler enda")
        return

    while True:
        utskrift_avtaler(avtale_lister, "Dine avtaler")
        index = input("Velg en avtale som skal vises: ")
        try:
            index = int(index)
            print(avtale_lister[index])
        except (ValueError, IndexError):
            print("Ugyldig index")
            input("Trykk en knapp for å prøve igjen...")
            continue
        break