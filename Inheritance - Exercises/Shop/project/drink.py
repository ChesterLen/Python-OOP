from project.product import Product


class Drink(Product):
    QUANTITY = 10

    def __init__(self, name: str) -> None:
        super().__init__(name, Drink.QUANTITY)