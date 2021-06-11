"""An animal base class."""


class Animal():
    """Class Animal"""
    def __init__(self, kind):
        self.kind = kind

    def get_kind(self):
        """Get kind of Animal"""
        return self.kind

    def make_sound(self):
        """Make a sound"""
        return f"{self.kind} sound"
