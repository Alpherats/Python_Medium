import re
import doctest


def some_txt(string: str) -> str:
    """
    Убирает из строки все нелатинское

    # возврат в нижнем регистре
    >>> some_txt('Hdkfps df')
    'hdkfps df'

    # возврат без кириллицы
    >>> some_txt("привет sthrn")
    ' sthrn'
    """

    return re.sub(r'[^a-zA-Z ]', '', string).lower()


if __name__ == '__main__':
    doctest.testmod(verbose=True)

#
