import pytest

from .shopping_list import ShoppingList
from .recipe import Recipe
from .ingredient import Ingredient
from .dietary_recipe import DietaryRecipe


def test_ingredient_init():
    ing = Ingredient("test_name", 67, "cm")
    assert ing.name == "test_name" and ing.quantity == 67 and ing.unit == "cm"

def test_ingredient_str():
    ing = Ingredient("test_name", 67, "cm")
    assert str(ing) == "test_name: 67.0 cm"

def test_ingredient_eq1():
    ing1 = Ingredient("name", 60, "cm")
    ing2 = Ingredient("name", 62, "cm")
    assert ing1 == ing2

def test_ingredient_eq2():
    ing1 = Ingredient("other", 62, "cm")
    ing2 = Ingredient("name", 62, "cm")
    assert ing1 != ing2

def test_ingredient_eq3():
    ing1 = Ingredient("name", 60, "m")
    ing2 = Ingredient("name", 62, "cm")
    assert ing1 != ing2