def discriminant(a, b, c):

    """Функция вычисляет корни квадратного уравнения"""

    D = b ** 2 - 4 * a * c
    if D == 0:
        result = f'{b*(-1) / (2 * a)}'
        return result
    elif D > 0:
        result_1 = (b*(-1) + D**0.5)/ (2 * a)
        result_2 = (b*(-1) - D**0.5) / (2 * a)
        result = (f'{result_1} {result_2}')
        return result
    else:
        result = 'корней нет'
        return result