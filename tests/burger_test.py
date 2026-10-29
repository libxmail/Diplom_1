import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_increases_list_length(self):
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_add_ingredient_adds_correct_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_decreases_list_length(self):
        burger = Burger()
        burger.add_ingredient(Mock())
        burger.add_ingredient(Mock())

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removes_correct_element(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()

        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        burger.remove_ingredient(0)

        assert burger.ingredients[0] == mock_ingredient_2

    @pytest.mark.parametrize(
        "index, expected_ingredient_index",
        [
            (0, 1),
            (1, 2),
            (2, 0),
        ],
    )
    def test_move_ingredient(self, index, expected_ingredient_index):
        burger = Burger()
        ingredients = [Mock(), Mock(), Mock()]

        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[index] == ingredients[expected_ingredient_index]

    def test_get_price(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ing_1 = Mock()
        mock_ing_1.get_price.return_value = 50

        mock_ing_2 = Mock()
        mock_ing_2.get_price.return_value = 30

        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)

        assert burger.get_price() == 280

    def test_get_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 50
        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n\n"
            "Price: 250"
        )

        assert burger.get_receipt() == expected_receipt