from ingredient import Ingredient

class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients
    def add_ingredient(self, ingredient: Ingredient):
        for other_ing in self.ingredients:
            if other_ing == ingredient:
                other_ing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return (isinstance(ratio, int) or  isinstance(ratio, float)) and ratio > 0

    def scale(self, ratio : float):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Некорректный коэффициент")

        new_recipe = Recipe(self.title, [])

        for ingredient in self.ingredients:
            new_recipe.add_ingredient(Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit))

        return new_recipe

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        result = f"{self.title}\n"

        for ingredient in self.ingredients:
            result += f"- {ingredient}\n"

        return result
