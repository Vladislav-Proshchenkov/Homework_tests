from unittest import TestCase
import vote


class Test_vote_with_params(TestCase):
    def test_vote_with_params(self):
        for i, (list_numbers, expected) in enumerate([
            ([1, 1, 2, 1, 1, 2, 2, 2, 3], '[1, 2]'),
            ([1, 1, 2, 3, 2, 2], '[2]'),
            ([], 'Список пустой'),
            (['один', 'два', 'три'], 'Некорректные данные')
        ]):
            with self.subTest(i):
                self.assertEqual(expected, vote.vote(list_numbers))
