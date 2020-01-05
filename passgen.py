"""
Генератор паролей
"""

from random import choice


def generate_password(password_length=12):
    """
    Генерация пароля с заданной длиной
    :param password_length: Длина пароля (по умолчанию 12 символов)
    :return: Случайный пароль заданной длины
    """

    if not password_length:
        password_length = 12

    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
               '4', '5', '6', '7', '8', '9', '0']

    password = []

    for i in range(password_length):
        password.append(choice(symbols))

    return "".join(password)


symbols_count = input('Введите количество символов (по умолчанию - 12): ')

if symbols_count:
    symbols_count = int(symbols_count)

print(generate_password(symbols_count))

input()
