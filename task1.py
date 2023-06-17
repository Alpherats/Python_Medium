# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

UP_BORDER = 10
LOW_BORDER = 2
INCLUDE_RIGHT_BORDER = 1

for i in range(LOW_BORDER, UP_BORDER):
    for j in range(LOW_BORDER, UP_BORDER + INCLUDE_RIGHT_BORDER):
        print(f"результат произведения {i} на {j} равен {i * j}")
