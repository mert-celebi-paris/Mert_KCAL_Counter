from unittest import TestCase

from module.exceptions import MealTooBigError
from module.functions import calorie_counter


class CaloriesCounterTestCase(TestCase):
    def test_count_meals_calories(self):
        result = calorie_counter(["meal-1, meal-2", "meal-3"])
        self.assertEqual(result, 1750, f"Expected 1750, got {result}")
        
    def test_count_meals_calories(self):
        result = calorie_counter(["combo-1, combo-2"])
        self.assertEqual(result, 1770, f"Expected 1750, got {result}")

    def test_count_meals_calories(self):
        result = calorie_counter(["meal-1, combo-1"])
        self.assertEqual(result, 1670, f"Expected 1670, got {result}")
    
    def test_raise_error_if_calories_too_big(self):
        with self.assertRaises(MealTooBigError) as e:
            calorie_counter (["combo-1", "combo-1"])
        self.assertEqual(
            e.exception.message,
            "Meal is too big! 2140 calories is too much!"
            "Wrong error message."
        )
