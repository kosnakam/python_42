class calculator:
    """A class implementing arithmetic operations"""
    def __init__(self, arg: list[float]):
        """Constructor of calculator class"""
        self.lst = arg

    def __add__(self, object) -> None:
        """Function of addition"""
        self.lst = [element + object for element in self.lst]
        print(self.lst)

    def __mul__(self, object) -> None:
        """Function of Multiplication"""
        self.lst = [element * object for element in self.lst]
        print(self.lst)

    def __sub__(self, object) -> None:
        """Function of Subtraction"""
        self.lst = [element - object for element in self.lst]
        print(self.lst)

    def __truediv__(self, object) -> None:
        """Function of Division"""
        try:
            self.lst = [element / object for element in self.lst]
            print(self.lst)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")