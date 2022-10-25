from datetime import datetime
import json


class Avtale:
    def __init__(self, tittel: str, sted: str, varighet_min: int, starttidspunkt: datetime) -> None:
        self.tittel = tittel
        self.sted = sted
        self.varighet_min = varighet_min
        self.starttidspunkt = starttidspunkt

    def __str__(self):
        return f"Avtale: {self.tittel}\nSted: {self.sted}\nVarighet: {self.varighet_min} min\nDato: {self.starttidspunkt}"


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


def lagre_liste(avtaler: list[Avtale]):
    """Lagrer ei liste med avtaler til en avtale fil"""

    # Gjør om til data som kan tolkes av json.dump
    avtale_dataer = []
    for avtale in avtaler:
        avtale_data = {}
        for key in avtale.__dict__:
            data = avtale.__dict__[key]

            # datetime objekter blir ikke tolket av json.dump
            # gjør dem om til streng verdier.
            if isinstance(data, datetime):
                avtale_data[key] = str(data)
                continue
            avtale_data[key] = data
        avtale_dataer.append(avtale_data)

    with open("avtale.txt", "w") as avtale_fil:
        json.dump(avtale_dataer, avtale_fil, indent=4, sort_keys=True)

def lese_fil(filnavn:str):
    """Leser inn avtaler fra en fil"""

    with open(filnavn, "r") as avtale_fil:
        avtaler_json = json.load(avtale_fil)
    
    # Konverterer fra tekst til en liste med avtale objekter
    avtaler_liste = []
    for avtale in avtaler_json:
        avtale['starttidspunkt'] = datetime.fromisoformat(avtale['starttidspunkt'])
        avtale = Avtale(**avtale)
        avtaler_liste.append(avtale)
    return avtaler_liste

def main():
    """Inngangen til programmet"""
    
if __name__ == "__main__":
    main()
