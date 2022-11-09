from json import JSONEncoder
from typing import Any


class StedEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__
