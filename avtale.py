from datetime import datetime

class Avtale:
    def __init__(self, tittel: str, sted: str, varighet_min: int, starttidspunkt: datetime ) -> None:
        self.tittel = tittel
        self.sted = sted
        self.varighet_min = varighet_min
        self.starttidspunkt = starttidspunkt
