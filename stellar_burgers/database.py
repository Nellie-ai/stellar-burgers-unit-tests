from .bun import Bun
from .ingredient import Ingredient
from .ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class Database:
    """In-memory demo catalogue used by the tests."""

    def __init__(self) -> None:
        self._buns = [
            Bun("sesame bun", 95),
            Bun("brioche bun", 125),
            Bun("rye bun", 110),
        ]
        self._ingredients = [
            Ingredient(INGREDIENT_TYPE_SAUCE, "barbecue sauce", 20),
            Ingredient(INGREDIENT_TYPE_SAUCE, "mustard sauce", 15),
            Ingredient(INGREDIENT_TYPE_SAUCE, "herb sauce", 25),
            Ingredient(INGREDIENT_TYPE_FILLING, "grilled patty", 80),
            Ingredient(INGREDIENT_TYPE_FILLING, "smoked tofu", 65),
            Ingredient(INGREDIENT_TYPE_FILLING, "crispy vegetables", 45),
        ]

    def available_buns(self) -> list[Bun]:
        return list(self._buns)

    def available_ingredients(self) -> list[Ingredient]:
        return list(self._ingredients)

