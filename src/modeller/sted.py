class Sted:
    def __init__(self, id: int, navn: str, gateadresse=None, postnummer=None, poststed=None) -> None:
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
