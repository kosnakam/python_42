class calculator:
    def __init__(self, V1: list[float], V2: list[float]):
        self.V1 = V1
        self.V2 = V2

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        output = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot produce is: {output}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]):
        output = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {output}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]):
        output = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {output}")
