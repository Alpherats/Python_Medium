# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

NUMBER_EXCEPTION_1 = 2
NUMBER_EXCEPTION_2 = 3
LEFT_BORDER = 0
RIGHT_BORDER = 100000
number = 5

if LEFT_BORDER < number < RIGHT_BORDER:
    if number % 1 == 0 and number % number == 0 \
            and (number % NUMBER_EXCEPTION_1 == 0 or number % NUMBER_EXCEPTION_2 == 0):
        print("Число составное")
    elif number % 1 == 0 and number % number == 0:
        print("Число простое")
else:
    print("Out of range!")
