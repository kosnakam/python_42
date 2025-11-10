class calculator:
    def __init__(self, arg: list[float]):
        self.lst = arg

    def __add__(self, object) -> None:
        self.lst = [element + object for element in self.lst]
        print(self.lst)

    def __mul__(self, object) -> None:
        self.lst = [element * object for element in self.lst]
        print(self.lst)

    def __sub__(self, object) -> None:
        self.lst = [element - object for element in self.lst]
        print(self.lst)

    def __truediv__(self, object) -> None:
        self.lst = [element / object for element in self.lst]
        print(self.lst)
