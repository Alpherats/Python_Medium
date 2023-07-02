# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента.
# (речь идет про **kwargs)

def return_lst(**kwargs) -> dict:
    '''принимает на вход только ключевые параметры и
     возвращает словарь, где ключ — значение переданного аргумента,
     а значение — имя аргумента'''
    dict = {}
    for key, value in kwargs.items():
        dict[value] = key
    return dict


print(return_lst(smth='sdd', new_num=5, lst='sd'))
