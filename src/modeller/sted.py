from utils.input_hjelper import hent_int


class Sted:
    def __init__(self, id: int, navn: str, gateadresse: str = None, postnummer: int = None, poststed: str = None) -> None:
        self.id = id
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.poststed = poststed

    def __str__(self) -> str:
        streng_konstruksjon = ''
        egenskap_dict = {'Id': self.id, 'Navn': self.navn, 'Gateadresse': self.gateadresse,
                         'Postnummer': self.postnummer, 'Poststed': self.poststed}
        for egenskap, verdi in egenskap_dict.items():
            if verdi:
                streng_konstruksjon += f'{egenskap}: {verdi}, '
        return streng_konstruksjon.rstrip(', ')


def lag_sted() -> Sted:
    """Lager et gyldig sted object"""

    navn = input("Skriv inn et stedsnavn: ")
    id = hent_int("Skriv inn en id :",
                  "Ugyldig ID, prøv igjen. Husk id er et tall")

    print("Ønsker du å oppgi adress [j/n]")
    svar = input(": ")
    if svar.lower() == "j":
        gateadresse = input("Venligst oppgi en gateadresse: ")
        postnummer = hent_int("Skriv inn et postnummer",
                              "Ugyldig postnummer, prøv igjen")
        poststed = input("Skriv inn et poststed: ")
        return Sted(id, navn, gateadresse, postnummer, poststed)

    return Sted(id, navn, gateadresse)
