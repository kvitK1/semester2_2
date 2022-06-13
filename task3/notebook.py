'''module to implement notebook'''


class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.

    Attributes:
    ------------
        memo: str
            content of the note
        tags: str
            tags of the note
        note_id: int
            id of the note
        owner: str
            creator of the note

    '''

    def __init__(self, memo, tags='', owner=''):
        '''initialize a note with memo and optional
        space-separated tags. Automatically set the note`s
        creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        Notebook.last_id += 1
        self.note_id = Notebook.last_id
        self.owner = owner

    def match(self, filt):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.'''
        return filt in self.memo or filt in self.tags


class Notebook:
    '''Represent a collection of notes that can be tagged,
       modified, and searched.

       Attributes:
       ------------
            notes: list
                list of notes

    '''

    last_id = 0

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo, tags='', owner=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags, owner))

    def modify_memo(self, note_id, memo, user, group):
        '''Find the note with the given id and change its
        memo to the given value.'''
        note = self._find_note(note_id)
        if note is not None:
            bol = self.check_if_user(note, user, group)
            if bol:
                note.memo = memo

    def modify_tags(self, note_id, tags, user, group):
        '''Find the note with the given id and change its
        tags to the given value.'''
        note = self._find_note(note_id)
        if note is not None:
            bol = self.check_if_user(note, user, group)
            if bol:
                note.tags = tags

    def search(self, filt):
        '''Find all notes that match the given filter
        string.'''
        notes = []
        for note in self.notes:
            if note.match(filt):
                notes.append(note)
        return notes

    @classmethod
    def check_if_user(cls, note, user, group):
        '''Check if user is creator of note or they are admin.'''
        if note.owner == user or group == "admin":
            return True
        return False

    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.note_id) == str(note_id):
                return note
        return None

    def delete_note(self, note_id, user, group):
        '''Delete the note by its id.'''
        note = self._find_note(note_id)
        if note is not None:
            bol = self.check_if_user(note, user, group)
            if bol:
                self.notes.remove(note)
                return True
        return False
