'''module to create the menu of notebook'''

from notebook import Notebook


class Menu:
    '''Class to represent notebook and working with its notes.

    Attributes:
    ------------
        notebook: Notebook
            example of Notebook class
        choices: dict
            dictionary with possible actions to choose from

    '''

    def __init__(self):
        '''Inits Menu with notebook, choices.'''
        self.notebook = Notebook()
        self.choices = {
                "show notes": self.show_notes,
                "add note": self.add_note,
                "modify note": self.modify_note,
                "search in notes": self.search_notes,
                "delete note": self.delete_notes,
            }

    def show_notes(self, notes=None):
        '''Shows the note and what it contains.'''
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.note_id}: {note.tags}\n{note.memo}\ncreator: {note.owner}\n")

    def search_notes(self):
        '''Searches for notes with a certain word.'''
        filt = input("Search for: ")
        notes = self.notebook.search(filt)
        if notes:
            self.show_notes(notes)
        else:
            print(f"Searching for [{filt}] in your notebook gave no results.")

    def add_note(self, owner):
        '''Adds new notes.'''
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        self.notebook.new_note(memo, tags, owner)
        print("Your note has been added.")

    def modify_note(self, i_d, memo, tags, owner, group):
        '''Modifies the note.'''
        if memo:
            self.notebook.modify_memo(i_d, memo, owner, group)
        if tags:
            self.notebook.modify_tags(i_d, tags, owner, group)
        print("Modifications ended.")

    def delete_notes(self, note_id, owner, group):
        '''Deletes the note.'''
        notes = self.notebook.notes
        if notes:
            dec = self.notebook.delete_note(note_id, owner, group)
            if dec:
                print("Your note has been deleted.")
            else:
                print("You have no permission to delete notes or there is no note with such id.")

note_book = Menu()
