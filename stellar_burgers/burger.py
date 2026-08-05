from typing import cast

from .bun import Bun
from .ingredient import Ingredient


class Burger:
    """A mutable burger assembled from one bun and ordered ingredients."""

    def __init__(self) -> None:
        self._bun: Bun | None = None
        self._ingredients: list[Ingredient] = []

    def set_buns(self, bun: Bun) -> None:
        self._bun = bun

    def add_ingredient(self, ingredient: Ingredient) -> None:
        self._ingredients.append(ingredient)

    def remove_ingredient(self, index: int) -> None:
        self._ingredients.pop(index)

    def move_ingredient(self, index: int, new_index: int) -> None:
        ingredient = self._ingredients.pop(index)
        self._ingredients.insert(new_index, ingredient)

    def get_price(self) -> float:
        bun = cast(Bun, self._bun)
        ingredient_total = sum(item.get_price() for item in self._ingredients)
        return bun.get_price() * 2 + ingredient_total

    def get_receipt(self) -> str:
        bun = cast(Bun, self._bun)
        lines = [f"(==== {bun.get_name()} ====)"]
        lines.extend(
            f"= {item.get_type().lower()} {item.get_name()} ="
            for item in self._ingredients
        )
        lines.append(f"(==== {bun.get_name()} ====)\n")
        lines.append(f"Price: {self.get_price()}")
        return "\n".join(lines)

