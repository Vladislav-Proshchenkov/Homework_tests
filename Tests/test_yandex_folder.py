import unittest
from unittest import TestCase
import yandex_add_folder as ya


class Test_ya_with_params(TestCase):

    def test_ya_with_params(self):
        for i, (folder_name, expected, expected_2) in enumerate([
            ('Папка', 201, 200),
            ('Папка', 409, 200),
            ('Папка_2', 201, 200)
        ]):
            with self.subTest(i):
                self.assertEqual(expected, ya.create_folder(folder_name))
                self.assertEqual(expected_2, ya.yandex_folder_exist(folder_name))
        ya.delete_folder('Папка')
        ya.delete_folder('Папка_2')


    @unittest.expectedFailure
    def test_ya_fail(self):
        folder_name = 'Папка_6'
        expected = 200
        self.assertEqual(expected, ya.yandex_folder_exist(folder_name))