from stellar_burgers.ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


BUN_TEST_CASES = (
    ("sesame bun", 95),
    ("brioche bun", 125.5),
)

INGREDIENT_TEST_CASES = (
    (INGREDIENT_TYPE_SAUCE, "barbecue sauce", 20),
    (INGREDIENT_TYPE_FILLING, "grilled patty", 80.5),
)

BURGER_BUN = BUN_TEST_CASES[0]
BURGER_INGREDIENTS = (
    INGREDIENT_TEST_CASES[0],
    INGREDIENT_TEST_CASES[1],
    (INGREDIENT_TYPE_SAUCE, "herb sauce", 25),
)

REMOVE_INGREDIENT_CASES = (
    (0, (1, 2)),
    (1, (0, 2)),
    (-1, (0, 1)),
)

MOVE_INGREDIENT_CASES = (
    (0, 2, (1, 2, 0)),
    (2, 0, (2, 0, 1)),
    (1, 1, (0, 1, 2)),
)

DATABASE_BUN_NAMES = ("sesame bun", "brioche bun", "rye bun")
DATABASE_BUN_PRICES = (95, 125, 110)
DATABASE_INGREDIENT_COUNT = 6
DATABASE_INGREDIENT_TYPE_COUNT = 3

EXPECTED_RECEIPT = (
    f"(==== {BURGER_BUN[0]} ====)\n"
    f"= {BURGER_INGREDIENTS[0][0].lower()} {BURGER_INGREDIENTS[0][1]} =\n"
    f"= {BURGER_INGREDIENTS[1][0].lower()} {BURGER_INGREDIENTS[1][1]} =\n"
    f"(==== {BURGER_BUN[0]} ====)\n"
    "\n"
    f"Price: {BURGER_BUN[1] * 2 + sum(item[2] for item in BURGER_INGREDIENTS[:2])}"
)

