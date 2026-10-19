from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_available_buns_returns_list_of_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        for bun in buns:
            assert isinstance(bun, Bun)

    def test_available_ingredients_returns_list_of_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)