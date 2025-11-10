from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Your docstring for Class"""
    def __init__(
            self, first_name, is_alive=True,
            family_name="Baratheon", eyes="brouwn", hairs="dark"
            ):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive, family_name, eyes, hairs)

    def set_eyes(self, arg: str) -> None:
        """This function sets self.eyes = arg"""
        self.eyes = arg

    def set_hairs(self, arg: str) -> None:
        """This function sets self.hairs = arg"""
        self.hairs = arg

    def get_eyes(self) -> None:
        """This function gets self.eyes"""
        return self.eyes

    def get_hairs(self) -> None:
        """This function gets self.hairs"""
        return self.hairs
