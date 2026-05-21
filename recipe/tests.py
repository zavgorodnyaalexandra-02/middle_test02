from django.test import TestCase
from recipe.models import Category, Recipe


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Dessert")
        self.assertEqual(category.name, "Dessert")
        self.assertEqual(str(category), "Dessert")

        # Перевіримо роботу __iter__
        items = list(iter(category))
        self.assertEqual(items, ["Dessert"])


class RecipeModelTest(TestCase):
    def test_recipe_creation(self):
        category = Category.objects.create(name="Main Dish")
        recipe = Recipe.objects.create(
            title="Borshch",
            description="Traditional Ukrainian soup",
            instructions="Boil, add vegetables, simmer",
            ingredients="Beetroot, cabbage, potatoes",
            category=category
        )
        self.assertEqual(recipe.title, "Borshch")
        self.assertEqual(recipe.category.name, "Main Dish")
        self.assertEqual(str(recipe), "Borshch")
        self.assertIsNotNone(recipe.created_at)
        self.assertIsNotNone(recipe.updated_at)
