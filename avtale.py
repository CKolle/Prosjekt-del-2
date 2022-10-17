from datetime import datetime
from multiprocessing.sharedctypes import Value

class Avtale:
    def __init__(self, tittel: str, sted: str, varighet_min: int, starttidspunkt: datetime ) -> None:
        self.tittel = tittel
        self.sted = sted
        self.varighet_min = varighet_min
        self.starttidspunkt = starttidspunkt

def lag_avtale()-> Avtale:
    """Lager et gyldig avtale objekt"""

    tittel = input("Venligst oppgi navnet på tittelen på avtalen: ")
    sted = input("Venglist oppgi stedet for avtalen: ")
    while True:
        try:
            varighet_min = int(input("Vengligst oppgi hvor lenge avtalen varer: ").replace(",","."))
        except ValueError:
            print("Ugyldig tall, prøv igjen")
            continue
        if varighet_min < 0:
            print("En avtale kan ikke vare mindre enn 0 minutter, prøv igjen")
            continue
        break

    while True:
        dato = input("Venglist oppgi dato for avtalen (DD.MM.ÅÅÅÅ): ").split(".")
        dag, maaende, aar = dato
        if len(dag) > 2 or len(maaende) > 2:
            print("Venligst oppgi en gyldig dato")
            continue
        if len(aar) > 4:
            print("Venligst oppgi en gyldig dato")
            continue
        try:
            dag = int(dag)
            maaende = int(maaende)
            aar = int(aar)
        except ValueError:
            print("Venglist oppgi en gyldig dato")
            continue
        break 

    while True:
        klokkeslett = input("Vengligst oppi et klokkelsett for avtalen (TT:MM): ").split(":")
        time, minutt = klokkeslett
        if len(time) > 2 or len(minutt) > 2:
            print("Venligst oppgi et gyldig klokkeslett")
            continue
        try:
            time = int(time)
            minutt = int(minutt)
        except ValueError:
            print("Venglisgt oppgi et gyldig klokkeslett")
            continue
        break
    starttidspunkt = datetime(aar, maaende, dag, time, minutt)
    return Avtale(tittel, sted, varighet_min, starttidspunkt)

def main():
    """Ingang til programmet"""
    ...

if __name__ == "__main__":
    main()
