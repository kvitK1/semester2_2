"""task4"""

import errors_for_string_editor as errors


class Character:
    """Class to represent a character and its features.

    Attributes:
    ------------
        character: str
            a character
        bold: bool
            if character is bold (True) or not (False)
        italic: bool
            if character is italic (True) or not (False)
        underline: bool
            if character is underlined (True) or not (False)

    """

    def __init__(self, character,
            bold=False, italic=False, underline=False):

        self.character = self.check_character(character)
        self.bold = bold
        self.italic = italic
        self.underline = underline

    @classmethod
    def check_character(cls, character):
        """Makes a character appropriate for following usage."""
        try:
            if len(character) > 1:
                raise errors.CharacterLengthException
        except errors.CharacterLengthException:
            return ""
        except TypeError:
            character = str(character)
            return cls.check_character(character)
        else:
            return character

    def __str__(self):
        bold = '*' if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold + italic + underline + self.character


class Cursor:
    """Class to represent a cursor and its ways.

    Attributes:
    ------------
        document: Document
            example of Document class
        position: int
            position of cursor (index of elements in list)

    """

    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        """Moves cursor forward."""
        self.position += 1

    def back(self):
        """Moves cursor backward."""
        self.position -= 1

    def home(self):
        """Moves cursor backward until \n occurs."""
        try:
            while self.document.characters[self.position-1].character != '\n':
                self.position -= 1
                if self.position == -1:
                    raise errors.InitialPositionachieved
        except errors.InitialPositionachieved:
            self.position = 0

    def end(self):
        """Moves cursor forward until \n occurs."""
        while self.position < len(self.document.characters)\
                and self.document.characters[self.position].character != '\n':
            self.position += 1


class Document:
    """Class to represent a document and its creating.

    Attributes:
    ------------
        characters: list
            list of characters
        cursor: Cursor
            example of Cursor class
        filename: str
            name of the file (where document is written)

    """

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        """Inserts character in the document."""
        try:
            if not isinstance(character, Character):
                raise errors.WrongAttributeValue
        except errors.WrongAttributeValue:
            character = Character(str(character))
        finally:
            self.characters.insert(self.cursor.position, character)
            self.cursor.forward()

    def delete(self):
        """Deletes character from some position."""
        try:
            del self.characters[self.cursor.position]
        except IndexError:
            self.characters = []

    def save(self):
        """Writes a file and saves info in it."""
        with open(self.filename, 'w', encoding="utf-8") as file:
            try:
                file.write(''.join(self.characters))
            except TypeError:
                file.write(''.join(str(c) for c in self.characters))

    def forward(self):
        """Moves cursor forward."""
        self.cursor += 1

    def back(self):
        """Moves cursor backward."""
        self.cursor -= 1

    @property
    def string(self):
        """Returns all characters together."""
        return "".join((str(c) for c in self.characters))


d = Document()
d.insert('h')
d.insert('e')
d.insert(Character('l', bold=True))
d.insert(Character('l', bold=True))
d.insert('o')
d.insert('\n')
d.insert(Character('w', italic=True))
d.insert(Character('o', italic=True))
d.insert(Character('r', underline=True))
d.insert('l')
d.insert('d')
print(f"small d: {d.string}")
d.cursor.home()
d.delete()
d.insert('W')
print(f"bid W: {d.string}")
d.characters[0].underline = True
print(d.string)
# d.filename='message.txt'
# d.save()
# print("done")
