# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
from math import pi

class Okr:
    def __init__(self, radius:float) -> None:
        self.radius = radius

    def length(self) -> float:
        answer = 2 * pi * self.radius
        return answer

    def square(self) -> float:
        answer = pi * self.radius**2
        return answer


first = Okr(10)
second  = Okr(20)
print(f"{first.length() = }, {first.square() = }")
print(f"{second.length() = }, {second.square() = }")