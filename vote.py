def vote(votes):

    """Функция принимает список целых чисел и возвращает
     число, которое встречается чаще всего."""

    votes_count = {}
    for i in votes:
        if type(i) != int:
            print(type(i))
            return 'Некорректные данные'
    if not votes:
        return 'Список пустой'
    for i in set(votes):
        votes_count[i] = votes.count(i)

    max_count_list = []
    max_count = max(votes_count.values())
    for i in votes_count:
        if votes_count[i] == max_count:
            max_count_list.append(i)
    return f'{max_count_list}'