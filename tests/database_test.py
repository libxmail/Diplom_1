import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_available_buns_returns_three_buns(self):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_available_buns_returns_bun_instances(self, index):
        db = Database()
        buns = db.available_buns()

        assert isinstance(buns[index], Bun)

    def test_available_ingredients_returns_six_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6

    @pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5])
    def test_available_ingredients_returns_ingredient_instances(self, index):
        db = Database()
        ingredients = db.available_ingredients()

        assert isinstance(ingredients[index], Ingredient)