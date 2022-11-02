from json import JSONEncoder
from typing import Any


class KategoriEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        o.prioritet = o.prioritet.value
        return o.__dict__
