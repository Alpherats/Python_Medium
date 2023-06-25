# Напишите программу, которая принимает две строки вида “a/b”- дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


fraction1 = "1/3"  # input("Insert 1: ")
fraction2 = "1/3"  # input("Insert 2: ")

numerator1 = int(fraction1[0])
denominator1 = int(fraction1[2])

numerator2 = int(fraction2[0])
denominator2 = int(fraction2[2])

nok = lcm(denominator1, denominator2)
frac_sum = f"{int(((numerator1 * nok / denominator1) + (numerator2 * nok / denominator2)))}/{nok}"
multiplicaion = f'{numerator1 * numerator2}/{denominator1 * denominator2}'

print(f'sum - {frac_sum}, multiplicaion - {multiplicaion}')
