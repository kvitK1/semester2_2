"""errors for string_editor."""


class InitialPositionachieved(Exception):
    """Exception: when position of cursor achieves -1."""


class WrongAttributeValue(Exception):
    """Exception: when something strange is passed as attribute to class."""


class CharacterLengthException(AssertionError):
    """Exception: when length of characters is bigger than 1."""
