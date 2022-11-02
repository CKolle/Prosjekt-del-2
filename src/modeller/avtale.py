from datetime import datetime
import json
from utils.json.AvtaleEncoder import AvtaleEncoder


class Avtale:
    def __init__(self, tittel: str, sted: str, varighet_min: int, starttidspunkt: datetime) -> None:
        self.tittel = tittel
        self.sted = sted
        self.varighet_min = varighet_min
        self.starttidspunkt = starttidspunkt

    def __str__(self):
        return f"Avtale: {self.tittel}\nSted: {self.sted}\nVarighet: {self.varighet_min} min\nDato: {self.starttidspunkt.strftime('%d.%m.%Y kl. %H:%M')}"


def lag_avtale() -> Avtale:
    """Lager et gyldig avtale objekt"""

    tittel = input("Vennligst oppgi navnet på tittelen på avtalen: ")
    sted = input("Vennligst oppgi stedet for avtalen: ")
    while True:
        try:
            varighet_min = int(
                input("Vengligst oppgi hvor lenge avtalen varer (minutter): ").replace(",", "."))
        except ValueError:
            print("Ugyldig tall, prøv igjen")
            continue
        if varighet_min < 0:
            print("En avtale kan ikke vare mindre enn 0 minutter, prøv igjen😂")
            continue
        break

    while True:
        dato = input(
            "Vennligst oppgi dato for avtalen (DD.MM.ÅÅÅÅ): ").split(".")
        try:
            dag, maanede, aar = dato
            dag = int(dag)
            maanede = int(maanede)
            aar = int(aar)

            # Ser om det er en gyldig dato
            datetime(aar, maanede, dag)
        except ValueError:
            print("Vennligst oppgi en gyldig dato")
            continue
        break

    while True:
        klokkeslett = input(
            "Vengligst oppi et klokkelsett for avtalen (TT:MM): ").split(":")
        try:
            time, minutt = klokkeslett
            time = int(time)
            minutt = int(minutt)
            starttidspunkt = datetime(aar, maanede, dag, time, minutt)
        except ValueError:
            print("Venglisgt oppgi et gyldig klokkeslett")
            continue
        break

    return Avtale(tittel, sted, varighet_min, starttidspunkt)


def utskrift_avtaler(avtaler: list[Avtale], overskrift=""):
    """Printer en liste med avtaler med indeks tittel og en felles overskrift"""

    if overskrift != "":
        print(overskrift)
    for avtale in avtaler:
        print(f"{avtaler.index(avtale)}: {avtale.tittel}")


def lagre_avtaler(avtaler: list[Avtale]):
    """Lagrer ei liste med avtaler til en avtale fil"""

    with open("avtale.txt", "w") as avtale_fil:
        json.dump(avtaler, avtale_fil, indent=4,
                  cls=AvtaleEncoder, sort_keys=True)


def les_avtaler(filnavn: str):
    """Leser inn avtaler fra en fil"""

    with open(filnavn, "r") as avtale_fil:
        avtaler_json = json.load(avtale_fil)

    # Konverterer fra tekst til en liste med avtale objekter
    avtaler_liste = []
    for avtale in avtaler_json:
        avtale['starttidspunkt'] = datetime.fromisoformat(
            avtale['starttidspunkt'])
        avtale = Avtale(**avtale)
        avtaler_liste.append(avtale)
    return avtaler_liste


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

    utskrift_avtaler(avtale_lister)

    while True:
        try:
            key = input("Hvilken avtale vil du slette: ")
            key = int(key)
            del avtale_lister[key]
        except (ValueError, IndexError):
            print("Oppgi gyldig avtale")
            continue
        break
    return avtale_lister


def endre_avtale(avtale_lister: list[Avtale]):
    """Spør brukeren om en avtale og lagter en ny avtale"""

    utskrift_avtaler(avtale_lister)

    while True:
        try:
            key = input("Hvilken avtale vil du endre: ")
            key = int(key)
            del avtale_lister[key]
        except (ValueError, IndexError):
            print("Oppgi gyldig avtale")
            continue
        break

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
