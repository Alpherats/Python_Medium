# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# BEFORE

TO_DECIMAL = 100


def extra_serializer(names: list[str],
                     salary: list[int],
                     extra: list[str]) -> dict:
    """Возвращает словарь премий."""

    extra_dict = {}
    for name, sal, ext in zip(names, salary, extra):
        extra_calc = float(ext.replace('%', '')) / TO_DECIMAL
        extra_dict[name] = sal * extra_calc
    return extra_dict


name_list = ['Vlad', 'Den', 'Alex']
salary_list = [1000, 2000, 3000]
extra_list = ['10.25%', '15%', '20%']

print(extra_serializer(name_list, salary_list, extra_list))

# AFTER

def create_bonus_dict(names, salary, bonus):
    return {name: salary * float(b.strip('%')) / 100 for name, salary, b in zip(names, salary, bonus)}


res = create_bonus_dict(name_list, salary_list, extra_list)

print(res)