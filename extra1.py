# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
import itertools


def fill_backpack(items: dict, max_weight: int) -> list:
    '''Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.'''

    backpack = []
    remaining_weight = max_weight

    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)

    for item, weight in sorted_items:
        if weight <= remaining_weight:
            backpack.append(item)
            remaining_weight -= weight

    return backpack


def get_all_variations(items: dict, max_weight: int) -> list:

    '''Верните все возможные варианты комплектации рюкзака.'''
    all_variations = []

    for r in range(1, len(items) + 1):
        for combination in itertools.combinations(items, r):
            total_weight = sum(items[item] for item in combination)
            if total_weight <= max_weight:
                all_variations.append(list(combination))

    return all_variations


backpack_items = {
    'спальный мешок': 1.5,
    'палатка': 2.5,
    'каримат': 0.8,
    'горелка': 0.3,
    'посуда': 1.0
}

target_weight = 4.0

result = fill_backpack(backpack_items, target_weight)
print(result)

# Верните все возможные варианты комплектации рюкзака.

result = get_all_variations(backpack_items, target_weight)
for variation in result:
    print(variation)
