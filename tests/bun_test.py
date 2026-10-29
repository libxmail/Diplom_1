import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("", 0),
            ("super-mega-long bun name", 999.99),
        ],
    )
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("", 0),
            ("super-mega-long bun name", 999.99),
        ],
    )
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price