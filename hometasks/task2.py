# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.
from random import randint


class GuessingMachine:
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    NUMBER_OF_ATTEMPTS = 10
    ADDITIONAL_NUMBER = 1

    def guess_number(self):
        num = randint(self.LOWER_LIMIT, self.UPPER_LIMIT)
        print(f"our number is {num}")
        tries = 0

        while tries < self.NUMBER_OF_ATTEMPTS:
            guess = int(input("Guess number: "))
            if tries == self.NUMBER_OF_ATTEMPTS - self.ADDITIONAL_NUMBER:
                print("U lose(((")
            elif guess == num:
                print("Congrats!")
                break
            elif guess > num:
                print(f"Wished number is lower, try again. Amount of tries left: "
                      f"{self.NUMBER_OF_ATTEMPTS - tries - self.ADDITIONAL_NUMBER}")
            elif guess < num:
                print(f"Wished number is bigger, try again. Amount of tries left:"
                      f" {self.NUMBER_OF_ATTEMPTS - tries - self.ADDITIONAL_NUMBER}")
            tries += 1


game = GuessingMachine()
game.guess_number()

