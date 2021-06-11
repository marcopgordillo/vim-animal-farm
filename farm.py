"""A farm for holding animals."""

class Farm():
    """Farm class"""

    def __init__(self):
        self.animals = set()

    def add_animal(self, animal):
        """Add an animal to animals set"""
        self.animals.add(animal)

    def print_contents(self):
        """print contents of the farm"""
        print("We've got some animals on the farm:",
              ', '.join(animal.get_kind() for animal in self.animals) + '.')
