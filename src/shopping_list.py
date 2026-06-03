from recipe import Recipe
from ingredient import Ingredient

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")

        scaled_recipe = recipe.scale(portions)

        for ingredient in scaled_recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        new_items = []

        for item in self._items:
            if item[1] != title:
                new_items.append(item)

        self._items = new_items

    def get_list(self):
        ingredients_dict = {}

        for ingredient, recipe_name in self._items:
            key = (ingredient.name, ingredient.unit)

            if key in ingredients_dict:
                ingredients_dict[key] += ingredient.quantity
            else:
                ingredients_dict[key] = ingredient.quantity

        result = []

        for (name, unit), quantity in ingredients_dict.items():
            result.append(
                Ingredient(name, quantity, unit)
            )

        result.sort(key=lambda ingredient: ingredient.name)

        return result

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items + other._items

        return new_list