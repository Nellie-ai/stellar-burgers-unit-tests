from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Ingredient:
    """A priced sauce or filling."""

    ingredient_type: str
    name: str
    price: float

    def get_type(self) -> str:
        return self.ingredient_type

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

