import os
import modeller.avtale as avtale_modell
import modeller.kategori as kategori_modell
import modeller.sted as sted_modell


def vis_meny():
    """Lager et meny system for alle kommandoer"""

    avtale_lister = []
    kategori_lister = []
    stedliste = []
    while True:
        print("Les inn filer [1]")
        print("Lag avtale [2]")
        print("Vis avtale [3]")
        print("Lagre [4]")
        print("Print avtaler [5]")
        print("Slett avtale [6]")
        print("Endre avtale [7]")
        print("Legg til kategori [8]")
        print("Legg til kategori til avtale[9]")
        print("Legg til sted [10]")
        print("Vis avtaler på sted [11]")
        print("Avslutt [12]")

        svar = input(": ")
        try:
            svar = int(svar)
        except ValueError:
            print("Prøv igjen")
            continue
        if svar == 1:
            kategori_lister, stedliste, avtale_lister = avtale_modell.les_avtaler(
                "avtale.txt")
        if svar == 2:
            lagre_avtale = avtale_modell.lag_avtale(stedliste)
            avtale_lister.append(lagre_avtale)
            print("Avtale lagd")
        if svar == 3:
            avtale_modell.vis_avtale(avtale_lister)
        if svar == 4:
            avtale_modell.lagre_avtaler(avtale_lister)
            sted_modell.lagre_sted(stedliste)
            kategori_modell.lagre_kategorier(kategori_lister)
            print("Lagret")
        if svar == 5:
            avtale_modell.utskrift_avtaler(avtale_lister)
        if svar == 6:
            avtale_modell.slett_avtale(avtale_lister)
            print("Avtale slettet")
        if svar == 7:
            avtale_modell.endre_avtale(avtale_lister)
            print("Avtale endret")
        if svar == 8:
            kategori = kategori_modell.lag_kategori()
            kategori_lister.append(kategori)
        if svar == 9:
            avtale_modell.legg_til_kategori(avtale_lister, kategori_lister)
        if svar == 10:
            sted = sted_modell.lag_sted()
            stedliste.append(sted)
        if svar == 11:
            avtaler_resultat = avtale_modell.finn_avtaler(
                stedliste, avtale_lister)
            avtale_modell.utskrift_avtaler(avtaler_resultat)
        if svar == 12:
            break

        input("Trykk en knapp for neste komando...")
        # Renser terminal vinduet
        os.system("cls||clear")


def main():
    """Inngangen til programmet"""
    vis_meny()


if __name__ == "__main__":
    main()
