from unittest import TestCase
import quadratic_equation as qe


class Test_qe_with_params(TestCase):
    def test_qe_with_params(self):
        for i, (a, b, c, expected) in enumerate([
            (1, 8, 15, '-3.0 -5.0'),
            (1, -13, 12, '12.0 1.0'),
            (-4, 28, -49, '3.5'),
            (1, 1, 1, 'корней нет')
        ]):
            with self.subTest(i):
                self.assertEqual(expected, qe.discriminant(a, b, c))
