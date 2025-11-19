import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Function generating id."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Data class"""
    name: str = ""
    surname: str = ""
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Initialize login and unique ID after the dataclass is created."""
        self.login = self.name[0] + self.surname
        self.id = generate_id()
