# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


class TypeOfTriangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def solve_triangle(self):
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            if self.a != self.b and self.b != self.c and self.a != self.c:
                return f'Есть разностороний со сторонами - {self.a}, {self.b}, {self.c}'
            elif self.a == self.b and self.b == self.c and self.a == self.c:
                return f'Есть равносторонний со сторонами - {self.a}, {self.b}, {self.c}'
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                return f'Есть равнобедренный со сторонами - {self.a}, {self.b}, {self.c}'
        else:
            return f"Нет такого треугольника"



first = TypeOfTriangle(10, 5, 6)
print(first.solve_triangle())

second = TypeOfTriangle(2,2,2)
print(second.solve_triangle())
