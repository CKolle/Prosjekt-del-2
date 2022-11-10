from json import JSONEncoder
from typing import Any
from utils.json.KategoriEncoder import KategoriEncoder


class AvtaleEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        o.starttidspunkt = str(o.starttidspunkt)

        o.kategorier = [] if o.kategorier is None else [
            kategori.id for kategori in o.kategorier]

        o.sted = o.sted.id
        return o.__dict__
