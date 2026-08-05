from unittest.mock import Mock

import pytest

from stellar_burgers.bun import Bun
from stellar_burgers.burger import Burger
from stellar_burgers.database import Database
from stellar_burgers.ingredient import Ingredient
from tests.data import BURGER_BUN, BURGER_INGREDIENTS


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun_mock():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = BURGER_BUN[0]
    bun.get_price.return_value = BURGER_BUN[1]
    return bun


@pytest.fixture
def ingredient_mocks():
    ingredients = []
    for ingredient_type, name, price in BURGER_INGREDIENTS:
        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        ingredients.append(ingredient)
    return ingredients


@pytest.fixture
def database():
    return Database()

