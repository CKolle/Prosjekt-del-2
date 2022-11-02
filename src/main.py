import os
from modeller.avtale import lag_avtale, les_avtaler, vis_avtale, lagre_avtaler, utskrift_avtaler, slett_avtale, endre_avtale


def vis_meny():
    """Lager et meny system for alle kommandoer"""

    avtale_lister = []
    while True:
        print("Les avtale fra fil [1]")
        print("Lag avtale [2]")
        print("Vis avtale [3]")
        print("Lagre avtaler til fil [4]")
        print("Print avtaler [5]")
        print("Slett avtale [6]")
        print("Endre avtale [7]")
        print("Avslutt [8]")

        svar = input(": ")
        try:
            svar = int(svar)
        except ValueError:
            print("Prøv igjen")
            continue
        if svar == 1:
            avtale_lister = les_avtaler("avtale.txt")
        if svar == 2:
            lagre_avtale = lag_avtale()
            avtale_lister.append(lagre_avtale)
            print("Avtale lagd")
        if svar == 3:
            vis_avtale(avtale_lister)
        if svar == 4:
            lagre_avtaler(avtale_lister)
            print("Avtale lagret")
        if svar == 5:
            utskrift_avtaler(avtale_lister)
        if svar == 6:
            slett_avtale(avtale_lister)
            print("Avtale slettet")
        if svar == 7:
            endre_avtale(avtale_lister)
            print("Avtale endret")
        if svar == 8:
            break

        input("Trykk en knapp for neste komando...")
        # Renser terminal vinduet
        os.system("cls||clear")


def main():
    """Inngangen til programmet"""
    vis_meny()


if __name__ == "__main__":
    main()
