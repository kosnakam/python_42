from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(
            self, first_name, is_alive=True,
            family_name="Baratheon", eyes="brouwn", hairs="dark"
            ):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """Call this in the parent class"""
        return super().__str__()

    def __repr__(self):
        """Call this in the parent class"""
        return super().__repr__()


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

    def __str__(self):
        """Call this in the parent class"""
        return super().__str__()

    def __repr__(self):
        """Call this in the parent class"""
        return super().__repr__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Your docstring for ClassMethod"""
        return cls(first_name, is_alive)
