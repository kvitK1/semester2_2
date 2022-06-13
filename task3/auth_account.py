"""main module for working with notebook programm."""

import auth
import menu1


user_roles = {
    "admin":
        ["login", "show notes", "add note", "search in notes",
            "give permissions",  "modify note", "delete note", "logout", "quit"],
    "editor":
        ["login", "show notes", "add note",
            "search in notes",  "modify note", "delete note", "logout", "quit"],
    "user":
        ["login", "show notes", "search in notes", "logout", "quit"]
    }

class User:
    '''Class to represent user, their process of working with notebook.

    Attributes:
    ------------
        username: str
            user`s name
        init_menu_map: dict
            choices, available for any type of users
        gen_menu_map: dict
            all possible actions to choose from
        menu_map: dict
            the main variant of user`s interface

    '''

    notes = {}
    counter = 1

    def __init__(self):
        """Inits User with username and different kinds of menus."""
        self.username = None
        self.init_menu_map = {
            "signup": self.signup,
            "login": self.login,
            "show notes": self.show_notes,
            "search in notes": self.search_notes,
            "quit": self.quit
        }
        self.gen_menu_map = {
            "signup": self.signup,
            "login": self.login,
            "show notes": self.show_notes,
            "add note": self.add_note,
            "search in notes": self.search_notes,
            "give permissions": self.give_perm,
            "delete note": self.delete_notes,
            "modify note": self.modify_note,
            "logout": self.logout,
            "quit": self.quit
        }
        self.menu_map = self.init_menu_map

    def create_menu(self, username, perms):
        """Create the appropriate menumap for users,
        according to their permissions."""
        new_map = {}
        try:
            if auth.authenticator.is_logged_in(username) and\
            auth.authenticator.users[username].group in perms:
                for_menu = perms[auth.authenticator.users[username].group][1:]
                new_map = {}
                for key, val in self.gen_menu_map.items():
                    if key in for_menu:
                        new_map[key] = val
            else:
                for key, val in self.init_menu_map.items():
                    new_map[key] = val
        except KeyError:
            for key, val in self.init_menu_map.items():
                new_map[key] = val
        return new_map

    @classmethod
    def signup(cls):
        """Manage process of signing up."""
        try:
            username = input("username: ")
            password = input("password: ")
            auth.authenticator.add_user(username, password)
            for key, val in auth.authenticator.users.items():
                if len(auth.authenticator.users) == 1:
                    val.group = "admin"
                else:
                    if val.group != "admin":
                        val.group = "user"
                perm = val.group
                permitions = user_roles[perm]
                for u_key, u_val in auth.authorizor.permissions.items():
                    if u_key in permitions:
                        u_val.add(key)
        except auth.UsernameAlreadyExists:
            print("Sorry, username is already used")
        except auth.PasswordTooShort:
            print("Sorry, password is too short.")

    def login(self):
        """Manange process of logging in."""
        logged_in = False
        # while not logged_in:
        username = input("username: ")
        password = input("password: ")
        try:
            logged_in = auth.authenticator.login(username, password)
        except auth.InvalidUsername:
            print("Sorry, that username does not exist")
        except auth.InvalidPassword:
            print("Sorry, incorrect password")
        else:
            self.username = username

    def logout(self):
        """Manage process of logging out."""
        logged_in = True
        try:
            logged_in = auth.authenticator.logout(self.username)
        except auth.InvalidUsername:
            print("Sorry, that username does not exist")
        else:
            self.username = None

    def is_permitted(self, permission):
        """Check if user is permitted to do some action."""
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as error:
            print("{} is not logged in".format(error.username))
            return False
        except auth.NotPermittedError as error:
            print("{} cannot {}".format(error.username, permission))
            return False
        else:
            return True

    def add_note(self):
        """Add note to the notebook."""
        if self.is_permitted("add note"):
            menu1.note_book.add_note(self.username)
        else:
            print("You have no permission to add notes.")

    @classmethod
    def search_notes(cls):
        """Search for some text in notes."""
        menu1.note_book.search_notes()

    def give_perm(self):
        """Admin method for giving logged_in users certain permissions."""
        if self.is_permitted("give permissions"):
            users_list = [el for el, val in auth.authenticator.users.items()]
            # if val.group != "admin"]
            roles = list(user_roles.keys())
            for u in users_list:
                print(u)
            answer = True
            user = ""
            perm = ""
            while answer:
                user = ""
                while user not in users_list:
                    user = input("enter a username: ")
                print(roles)
                perm = ""
                while perm not in roles:
                    perm = input(f"what userrole you want to give to [{user}]? ")
                answer = False
            auth.authenticator.users[user].group = perm
            permitions = user_roles[perm]
            for key, val in auth.authorizor.permissions.items():
                if key in permitions:
                    val.add(user)
        else:
            print("You have to be an admin.")

    def modify_note(self):
        """Modify notes, their memos and/or tags."""
        if self.is_permitted("modify note"):
            i_d = input("Enter a note id: ")
            memo = input("Enter a memo: ")
            tags = input("Enter tags: ")
            menu1.note_book.modify_note(i_d, memo, tags, self.username,
            auth.authenticator.users[self.username].group)
        else:
            print("You have no permission to modify notes.")

    def delete_notes(self):
        """Delete note by its id."""
        if self.is_permitted("delete note"):
            note_id = input("Enter a note id: ")
            menu1.note_book.delete_notes(note_id, self.username,
            auth.authenticator.users[self.username].group)

    @classmethod
    def show_notes(cls):
        """Show all notes, created by users."""
        menu1.note_book.show_notes()

    @classmethod
    def quit(cls):
        """Ends working with notebook."""
        raise SystemExit()

    def menu(self):
        """Manage the process of notebook usage."""
        for func in self.gen_menu_map:
            auth.authorizor.add_permission(func)
        try:
            answer = ""
            while True:
                self.menu_map = self.create_menu(self.username, user_roles)
                print("\n")
                for action in self.menu_map:
                    print(action)
                if auth.authenticator.is_logged_in(self.username):
                    print("\n___USERS___")
                    if self.username is not None:
                        print(f"temporary user: {self.username}\n")
                    for user in auth.authenticator.users.values():
                        print(f"{user.username}: {user.group}")
                try:
                    answer = input("\nenter a command: ").lower()
                    func = self.menu_map[answer]
                except KeyError:
                    print(f"{answer} is not a valid option")
                else:
                    func()
        finally:
            print("Thank you for using the notebook!")

User().menu()
