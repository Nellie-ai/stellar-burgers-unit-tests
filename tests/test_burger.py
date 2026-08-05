import pytest

from tests.data import (
    BURGER_BUN,
    BURGER_INGREDIENTS,
    EXPECTED_RECEIPT,
    MOVE_INGREDIENT_CASES,
    REMOVE_INGREDIENT_CASES,
)


class TestBurger:
    def test_get_price_without_ingredients_returns_double_bun_price(
        self,
        burger,
        bun_mock,
    ):
        burger.set_buns(bun_mock)

        assert burger.get_price() == BURGER_BUN[1] * 2
        bun_mock.get_price.assert_called_once_with()

    def test_add_ingredient_includes_ingredient_in_price(
        self,
        burger,
        bun_mock,
        ingredient_mocks,
    ):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mocks[0])

        expected_price = BURGER_BUN[1] * 2 + BURGER_INGREDIENTS[0][2]
        assert burger.get_price() == expected_price
        ingredient_mocks[0].get_price.assert_called_once_with()

    @pytest.mark.parametrize("index, expected_indices", REMOVE_INGREDIENT_CASES)
    def test_remove_ingredient_excludes_item_from_price(
        self,
        burger,
        bun_mock,
        ingredient_mocks,
        index,
        expected_indices,
    ):
        burger.set_buns(bun_mock)
        for ingredient in ingredient_mocks:
            burger.add_ingredient(ingredient)

        burger.remove_ingredient(index)

        expected_price = BURGER_BUN[1] * 2 + sum(
            BURGER_INGREDIENTS[item_index][2]
            for item_index in expected_indices
        )
        assert burger.get_price() == expected_price
        for item_index, ingredient in enumerate(ingredient_mocks):
            if item_index in expected_indices:
                ingredient.get_price.assert_called_once_with()
            else:
                ingredient.get_price.assert_not_called()

    @pytest.mark.parametrize(
        "index, new_index, expected_indices",
        MOVE_INGREDIENT_CASES,
    )
    def test_move_ingredient_changes_order_in_receipt(
        self,
        burger,
        bun_mock,
        ingredient_mocks,
        index,
        new_index,
        expected_indices,
    ):
        burger.set_buns(bun_mock)
        for ingredient in ingredient_mocks:
            burger.add_ingredient(ingredient)

        burger.move_ingredient(index, new_index)

        receipt = burger.get_receipt()
        ingredient_positions = [
            receipt.index(BURGER_INGREDIENTS[item_index][1])
            for item_index in expected_indices
        ]
        assert ingredient_positions == sorted(ingredient_positions)

    def test_get_price_with_ingredients_returns_total(
        self,
        burger,
        bun_mock,
        ingredient_mocks,
    ):
        burger.set_buns(bun_mock)
        for ingredient in ingredient_mocks[:2]:
            burger.add_ingredient(ingredient)

        expected_price = BURGER_BUN[1] * 2 + sum(
            item[2] for item in BURGER_INGREDIENTS[:2]
        )
        assert burger.get_price() == expected_price

    def test_get_receipt_returns_formatted_receipt(
        self,
        burger,
        bun_mock,
        ingredient_mocks,
    ):
        burger.set_buns(bun_mock)
        for ingredient in ingredient_mocks[:2]:
            burger.add_ingredient(ingredient)

        assert burger.get_receipt() == EXPECTED_RECEIPT

