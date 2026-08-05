from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Bun:
    """A bun selected for a burger."""

    name: str
    price: float

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

