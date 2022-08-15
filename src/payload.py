import json
import datetime
import dataclasses

from typing import Optional

from .constants import *
from .utils import Serializable


@dataclasses.dataclass
class Payload(Serializable):
    """Payload structure to used to query the Zomato API"""

    res_ids: list[int]
    end_date: Optional[str] = None
    count: int = 20
    offSet: int = 0
    state: str = "DELIVERED"

    def __post_init__(self):
        if self.end_date is None:
            self.end_date = datetime.datetime.now().strftime(DATE_FORMAT)

    @property
    def start_date(self) -> str:
        return (
            datetime.datetime.strptime(self.end_date, DATE_FORMAT)
            - datetime.timedelta(days=10)
        ).strftime(DATE_FORMAT)

    def to_json(self) -> str:
        """Convert payload instance to a JSON string"""
        return json.dumps(dataclasses.asdict(self) | {"start_date": self.start_date})
