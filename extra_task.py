# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
NUMBER_OF_ATTEMPTS = 10
ADDITIONAL_NUMBER = 1

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f"our number is {num}")
tries = 0

while tries < NUMBER_OF_ATTEMPTS:
    guess = int(input("Guess number: "))
    if tries == NUMBER_OF_ATTEMPTS - ADDITIONAL_NUMBER:
        print("U lose(((")
    elif guess == num:
        print("Congrats!")
        break
    elif guess > num:
        print(f"Wished number is lower, try again. Amount of tries left: "
              f"{NUMBER_OF_ATTEMPTS - tries - ADDITIONAL_NUMBER}")
    elif guess < num:
        print(f"Wished number is bigger, try again. Amount of tries left:"
              f" {NUMBER_OF_ATTEMPTS - tries - ADDITIONAL_NUMBER}")
    tries += 1
