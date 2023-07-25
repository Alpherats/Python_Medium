class Human:
    def __init__(self, fio: str, age: int or float) -> None:
        self.fio = fio
        self._age = age


    def __str__(self) -> str:
        return f"{self.fio}, age - {self._age}"

    def birthday(self):
        self._age += 1




# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

class Worker(Human):
    CONST = 7
    def __init__(self, fio: str, age: int or float, id: int) -> None:
        super().__init__(fio, age)
        self.id = id
        self.lvl_access = id % self.CONST



man = Human("Valera", 20)

print(man)


worker1 = Worker('Alex',20 ,123455)

print(f"{worker1.lvl_access = }")
