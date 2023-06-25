# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


BORDER = 0
DEVIDER = 16
num: int = 4597
num_for_hex = num
hex_table = {
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F",
    "16": "G"
}

res = ''
while num > BORDER:

    divided = num % DEVIDER
    if divided >= 10:
        res += hex_table[str(divided)]
    else:
        res += str(num % DEVIDER)
    num //= DEVIDER

res = res[::-1]
print(f"0x{res}, {hex(num_for_hex)}")
