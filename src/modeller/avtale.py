from datetime import datetime
from utils.input_hjelper import hent_int, hent_datoklokkeslett
import json
from utils.json.AvtaleEncoder import AvtaleEncoder
from modeller.kategori import *
from modeller.sted import *


class Avtale:
    def __init__(self, tittel: str, sted: Sted, varighet_min: int, starttidspunkt: datetime, kategorier: list[Kategori] = []) -> None:
        self.tittel = tittel
        self.sted = sted
        self.varighet_min = varighet_min
        self.starttidspunkt = starttidspunkt
        self.kategorier = kategorier

    def __str__(self):
        return f"Avtale: {self.tittel}\nSted: {self.sted.navn}\nVarighet: {self.varighet_min} min\nDato: {self.starttidspunkt.strftime('%d.%m.%Y kl. %H:%M')}\n kategorier: {[str(x.navn) for x in self.kategorier]}"

    def legg_til_kategori(self, kategori: Kategori):
        if self.kategorier:
            self.kategorier.append(kategori)


def lag_avtale(steder: list[Sted]) -> Avtale:
    """Lager et gyldig avtale objekt"""

    tittel = input("Vennligst oppgi navnet på tittelen på avtalen: ")
    varighet_min = hent_int(
        "Vengligst oppgi hvor lenge avtalen varer (minutter): ", "Ugyldig tall, prøv igjen", 1)
    starttidspunkt = hent_datoklokkeslett()

    if not steder:
        print("Du har ingen steder i systemet")
        print("Lager sted")
        sted = lag_sted()
        steder.append(sted)
        return Avtale(tittel, sted, varighet_min, starttidspunkt)

    print("Eksisterende steder")
    utskrift_stedliste(steder)
    svar = input("Vil du bruke et eksisterende sted [j/n]?")
    if svar.lower() == "n":
        sted = lag_sted()
        steder.append(sted)
        return Avtale(tittel, sted, varighet_min, starttidspunkt)

    print("Venligst velg et sted")
    min = 0
    max = len(steder) - 1
    sted_i = hent_int(": ", "Ugyldig sted, prøv igjen",
                      min, max, utskrift_stedliste, steder)
    sted = steder[sted_i]

    return Avtale(tittel, sted, varighet_min, starttidspunkt)


def legg_til_kategori(avtaler: list[Avtale], kategorier: list[Kategori]):
    if not kategorier:
        print("Du har ingen lagrede kategorier, lag en og prøv igjen")
        return
    min = 0
    max = len(avtaler) - 1
    print("Velg en avtale")
    i_avtale = hent_int(": ", "prøve igjen", min, max,
                        utskrift_avtaler, avtaler)
    max = len(kategorier) - 1
    print("Velg en kateogri")
    i_kategori = hent_int(": ", "prøv igjen", min, max,
                          utskrift_kategorier, kategorier)
    avtaler[i_avtale].legg_til_kategori(kategorier[i_kategori])


def utskrift_avtaler(avtaler: list[Avtale], overskrift: str = None):
    """Printer en liste med avtaler med indeks tittel og en felles overskrift"""

    if overskrift:
        print(overskrift)
    for avtale in avtaler:
        print(f"{avtaler.index(avtale)}: {avtale.tittel}")


def finn_avtaler(stedliste: list[Sted], avtaler: list[Avtale]) -> list[Avtale]:
    if not stedliste or not avtaler:
        print("Du har ingen sted eller avtaler ennda")
        return []
    min = 0
    max = len(stedliste) - 1
    sted_i = hent_int("Velg et sted: ", "Prøv igjen", min,
                      max, utskrift_stedliste, stedliste)
    sted = stedliste[sted_i]
    filtrert = filter(lambda avtale: avtale.sted.id == sted.id, avtaler)
    return list(filtrert)


def lagre_avtaler(avtaler: list[Avtale], kategorier: list[Kategori] = None, steder: list[Sted] = None):
    """Lagrer ei liste med avtaler, filer og steder til filer"""
    if kategorier:
        lagre_kategorier(kategorier)
    if steder:
        lagre_sted(steder)
    with open("avtale.txt", "w") as avtale_fil:
        json.dump(avtaler, avtale_fil, indent=4,
                  cls=AvtaleEncoder, sort_keys=True)


def les_avtaler(filnavn_avtaler: str):
    """Leser inn avtaler, kategorier og steder fra filer"""

    kategorier_liste = les_kategorier()

    stedliste = les_sted()

    with open(filnavn_avtaler, "r") as avtale_fil:
        avtaler_json = json.load(avtale_fil)

    # Konverterer fra tekst til en liste med avtale objekter
    avtaler_liste: list[Avtale] = []
    for avtale in avtaler_json:
        avtale['starttidspunkt'] = datetime.fromisoformat(
            avtale['starttidspunkt'])

        avtale["kategorier"] = [soek_kategorier(
            id) for id in avtale["kategorier"]]

        avtale["sted"] = soek_sted(stedliste, avtale["sted"])

        avtale = Avtale(**avtale)
        avtaler_liste.append(avtale)

    return (kategorier_liste, stedliste, avtaler_liste)


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
