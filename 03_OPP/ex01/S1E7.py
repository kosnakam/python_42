from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(
            self, first_name, is_alive=True,
            family_name="Lannister", eyes="blue", hairs="light"
            ):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Your docstring for ClassMethod"""
        return cls(first_name, is_alive)
