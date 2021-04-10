from unittest import TestCase
import training_functions as tf


class TrainingFunctionTests(TestCase):
    def test_calculate_ninety(self):
        ninety = tf.calculate_ninety(100)
        self.assertEqual(ninety, 90.0)

    def test_calculate_max_weight(self):
        max_weight = tf.calculate_max_weight(75, 5)
        print(max_weight)
        self.assertEqual(max_weight, 84.4)

    def test_calc_percentage(self):
        percentage = tf.calc_percentage(100, 81.3)
        self.assertEqual(percentage, 81)
