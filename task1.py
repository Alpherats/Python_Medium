# дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# Пример:
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

def find_duplicates(lst: list) -> list:
    '''дан список повторяющихся элементов. Вернуть список с дублирующимися элементами'''

    duplicates = []
    unique_elements = set()

    for item in lst:
        if item in unique_elements:
            if item not in duplicates:
                duplicates.append(item)
        else:
            unique_elements.add(item)

    return duplicates


my_list = [1, 2, 3, 1, 2, 4, 5]
result = find_duplicates(my_list)
print(result)
