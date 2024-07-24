from unittest import TestCase
import secretary as sec


class Test_secretary_with_params(TestCase):
    def test_get_name_with_params(self):
        for i, (doc_number, expected) in enumerate([
            ('10006', 'Аристарх Павлов'),
            ('2207 876234', 'Василий Гупкин'),
            ('', 'Документ не найден'),
            ('67546548', 'Документ не найден')
        ]):
            with self.subTest(i):
                self.assertEqual(expected, sec.get_name(doc_number))

    def test_get_directory_with_params(self):
        for i, (doc_number, expected) in enumerate([
            ('11-2', '1'),
            ('849651651', 'Полки с таким документом не найдено'),
            ('', 'Полки с таким документом не найдено'),
            ('10006', '2')
        ]):
            with self.subTest(i):
                self.assertEqual(expected, sec.get_directory(doc_number))

    def test_add_with_params(self):
        for i, (document_type, number, name, shelf_number, expected) in enumerate([
            ('international passport', '311 020203', 'Александр Пушкин', 3, 'Документ добавлен'),
            ('passport', '', 'Василий Иванов', 2, 'Некорректный номер документа'),
            ('insurance', '12345', 'Геннадий Покемонов', '2', 'Некорректный номер полки'),
            ('passport', '2207 876234', 'Василий Гупкин', 1, 'Документ уже существует')
        ]):
            with self.subTest(i):
                self.assertEqual(expected, sec.add(document_type, number, name, shelf_number))
