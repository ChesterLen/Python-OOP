class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient in self.ingredients.keys():
                self.ingredients[ingredient] += quantity
                self.price += price_per_quantity * quantity
            else:
                self.ingredients[ingredient] = quantity
                self.price += price_per_quantity * quantity
        
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient not in self.ingredients.keys():
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            elif ingredient in self.ingredients.keys():
                if quantity > self.ingredients[ingredient]:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.price -= (quantity * price_per_quantity)
                    self.ingredients[ingredient] -= quantity

        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        if not self.ordered:
            self.ordered = True
            ingrediants_list = []
            for item, value in self.ingredients.items():
                ingrediants_list.append(f"{item}: {value}")
            return f"You've ordered pizza {self.name} prepared with {', '.join(ingrediants_list)} and the price will be {self.price}lv."

        return f"Pizza {self.name} already prepared, and we can't make any changes!"