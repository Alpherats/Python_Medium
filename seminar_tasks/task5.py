# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age


class Fishes(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 jabry: bool,
                 size: str) -> None:
        super().__init__(name, age)
        self.jabry = jabry
        self.size = size

    def __str__(self):
        return f"{self.jabry}, {self.size}"


class Birds(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 wings: bool) -> None:
        super().__init__(name, age)
        self.wings = wings

    def __str__(self):
        return f"{self.wings}"


forel = Fishes('forel', 10, True, 'small')
print(forel)
eagle = Birds('eagle', 1, True)
print(eagle)
