class calculator:
    """A class implementing arithmetic operations"""
    def __init__(self, V1: list[float], V2: list[float]):
        """Constructor of calculator class"""
        self.V1 = V1
        self.V2 = V2

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Function of dotproduct"""
        output = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot produce is: {output}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]):
        """Function of add_vec"""
        output = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {output}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]):
        """Function of sous_vec"""
        output = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {output}")
