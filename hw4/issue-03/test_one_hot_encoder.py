from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_fit_transform_equals(self):
        self.assertEqual(fit_transform(['a', 'b', 'a']), [
            ('a', [0, 1]),
            ('b', [1, 0]),
            ('a', [0, 1])
        ])

    def test_fit_transform_equals_scnd(self):
        self.assertEqual(fit_transform('Hello'), [('Hello', [1])])

    def test_fit_transform_istrue(self):
        actual_result = fit_transform([
            'Moscow', 'New York', 'Moscow', 'London'
        ])

        expected_result = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0])
        ]

        self.assertTrue(actual_result, expected_result)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            fit_transform(123)
