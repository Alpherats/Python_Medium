# Фибоначи


def fibo(n: int) -> int:
    '''Вывод n-ого числа фибоначи'''
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def fibonacci_generator() -> int:
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()

for _ in range(13):
    print(next(fib))

print(fibo(7))
