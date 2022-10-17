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
            varighet_min = int(input("Vengligst oppgi hvor lenge avtalen varer (minutter): ").replace(",","."))
        except ValueError:
            print("Ugyldig tall, prøv igjen")
            continue
        if varighet_min < 0:
            print("En avtale kan ikke vare mindre enn 0 minutter, prøv igjen😂")
            continue
        break

    while True:
        dato = input("Venglist oppgi dato for avtalen (DD.MM.ÅÅÅÅ): ").split(".")
        try:
            dag, maanede, aar = dato
            dag = int(dag)
            maanede = int(maanede)
            aar = int(aar)

            #Ser om det er en gyldig dato
            datetime(aar, maanede, dag)
        except ValueError:
            print("Venglist oppgi en gyldig dato")
            continue
        break 

    while True:
        klokkeslett = input("Vengligst oppi et klokkelsett for avtalen (TT:MM): ").split(":")
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

def main():
    """Inngangen til programmet"""

if __name__ == "__main__":
    main()
