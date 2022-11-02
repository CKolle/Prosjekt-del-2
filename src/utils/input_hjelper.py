from datetime import datetime
from typing import Callable


def hent_int(melding: str, error_melding: str, min: int = None, max: int = None, pre_printfunk: Callable = None, *args) -> int:
    IGJEN_MELDING = "Trykk på en knapp for å prøve igjen..."

    while True:

        if pre_printfunk is not None:
            pre_printfunk(*args)

        tall = input(melding)
        try:
            tall = int(tall)
        except ValueError:
            print(error_melding)
            input(IGJEN_MELDING)
            continue

        if min is not None and tall < min:
            print(error_melding)
            input(IGJEN_MELDING)
            continue

        if max is not None and tall > max:
            print(error_melding)
            input(IGJEN_MELDING)
            continue

        return tall


def hent_datoklokkeslett() -> datetime:

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
            input("Trykk på en knapp for å prøve igjen...")
            continue
        break

    while True:
        klokkeslett = input(
            "Vengligst oppi et klokkelsett for avtalen (TT:MM): ").split(":")
        try:
            time, minutt = klokkeslett
            time = int(time)
            minutt = int(minutt)
            datoklokkeslett = datetime(aar, maanede, dag, time, minutt)
        except ValueError:
            print("Venglisgt oppgi et gyldig klokkeslett")
            input("Trykk på en knapp for å prøve igjen...")
            continue
        return datoklokkeslett
