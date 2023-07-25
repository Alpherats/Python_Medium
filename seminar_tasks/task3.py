class Rectangle:
    def __init__(self, length: float, width: float or None = None) -> None:
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length
    def per(self) -> float:
        answer = self.length * 2 + self.width * 2
        return answer
    def square(self) -> float:
       answer = self.length * self.width
       return answer


