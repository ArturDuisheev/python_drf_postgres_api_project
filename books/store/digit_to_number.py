def number_digit(number: int) -> str:
    """Разбивает целое число number на строку в виде суммы чисел по разрядам"""

    # Проверяем положительное ли число
    if number < 0:
        raise ValueError('Число должно быть положительным')
    #  Если число меньше или равно 10 то его сразу помещают в строку
    if number <= 10:
        return str(number)

    # Список для элементов числа
    final_str = []

    # Циклом проходим по разрядам от самого большого и значение каждого разряда помещаем в список,
    # после чего уменьшаем начального число на данный разряд
    for i in range(len(str(number)), 0, -1):
        cur_dig = (str((number // 10 ** (i - 1)) * 10 ** (i - 1)))
        number -= int(cur_dig)
        final_str.append(cur_dig)

    return ' + '.join(final_str)


if __name__ == '__main__':
    print(number_digit(-2))