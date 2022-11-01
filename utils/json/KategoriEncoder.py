import json
from typing import Any


class KategoriEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        o.prioritet = o.prioritet.value
        return o.__dict__
