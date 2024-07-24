documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }


def get_name(doc_number):

    """Функция возвращает имя исполнителя по номеру документа"""

    for numbers in documents:
        if doc_number == numbers['number']:
            return numbers['name']
    return 'Документ не найден'

def get_directory(doc_number):

    """Функция возвращает номер полки по номеру документа"""

    for shelf, number_doc in directories.items():
        if doc_number in number_doc:
            return shelf
    return 'Полки с таким документом не найдено'

def add(document_type, number, name, shelf_number):

    """Функция добавляет новый документ в каталог и в перечень полок"""

    for i in directories.values():
        if number in i:
            return 'Документ уже существует'

    new_record = {"type": document_type, 'number': number,'name': name}

    if document_type == '' and type(document_type) != str:
        return 'Некорректный тип документа'
    if number == '':
        return 'Некорректный номер документа'
    if name == '' and type(name) != str:
        return 'Некорректное имя'
    if type(shelf_number) != int:
        return 'Некорректный номер полки'

    documents.append(new_record)
    new_direct = [str(number)]
    directories[shelf_number] = new_direct

    return 'Документ добавлен'