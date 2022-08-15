import requests
import dataclasses

from .payload import Payload
from .configurator import Config


@dataclasses.dataclass
class FoodItem:

    name: str
    cost: float
    quantity: int

    @classmethod
    def from_dict(cls, data: dict) -> "FoodItem":
        return cls(name=data["name"], cost=data["unitCost"], quantity=data["quantity"])

    @property
    def total_cost(self) -> float:
        return self.cost * self.quantity


@dataclasses.dataclass
class Order:

    id: int
    date: str
    customer: str
    items: list[FoodItem] = dataclasses.field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> "Order":

        date = data["createdAt"].split("T")[0]
        items = [FoodItem.from_dict(item) for item in data["items"]["dishes"]]

        return cls(
            date=date,
            items=items,
            id=data["id"],
            customer=data["creator"]["name"],
        )

    def __len__(self) -> int:
        return len(self.items)


def get_orders(url: str, payload: Payload, config: Config) -> list[Order]:
    req = requests.post(
        url,
        data=payload,
        headers=config.headers,
        cookies=config.cookies,
    )
    return [Order.from_dict(order) for order in req.json()["orders"]]
