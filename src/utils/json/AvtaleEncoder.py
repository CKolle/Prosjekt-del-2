from json import JSONEncoder
from typing import Any


class AvtaleEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        o.starttidspunkt = str(o.starttidspunkt)
        return o.__dict__
