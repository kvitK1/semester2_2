'''module to create main functions for authorization and authentication.'''

import hashlib


class AuthException(Exception):
    '''Class to represent main and general exceptions for further usage.

    Attributes:
    ------------
        username: str
            user`s name
        user: User
            example of User class

    '''

    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    '''UsernameAlreadyExists exception.'''

    def __str__(self):
        return f"[{self.username}] already exists."


class PasswordTooShort(AuthException):
    '''PasswordTooShort exception.'''

    def __str__(self):
        return "Password is too short."


class InvalidUsername(AuthException):
    '''InvalidUsername exception.'''

    def __str__(self):
        return f"Invalid username: [{self.username}]."


class InvalidPassword(AuthException):
    '''InvalidPassword exception.'''

    def __str__(self):
        return "Invalid password. Try again."


class PermissionError(Exception):
    '''PermissionError exception.'''

    def __str__(self):
        return "Permission error occurred."


class NotLoggedInError(AuthException):
    '''NotLoggedInError exception.'''

    def __str__(self):
        return f"[{self.username}], you aren`t logged in."


class NotPermittedError(AuthException):
    '''NotPermittedError exception.'''
    def __str__(self):
        return f"[{self.username}], you have no permission for that."


class User:
    '''Class to represent user, their username and password info.

    Attributes:
    ------------
        username: str
            user`s name
        group: str
            user`s role
        password: str
            encrypted password
        is_logged_in: bool
            is user is logged in (True) or not (False)

    '''

    def __init__(self, username, password):
        """Create a new user object. The password
        will be encrypted before storing."""
        self.username = username
        self.group = None
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return
        the sha digest."""
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for this
        user, false otherwise."""
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class Authenticator:
    '''Class to represent authentication process.

    Attributes:
    ------------
        users: dict
            dictionary with users` info

    '''

    def __init__(self):
        """Construct an authenticator to manage
        users logging in and out."""
        self.users = {}

    def add_user(self, username, password):
        """Add user to dict with users."""
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        """Action of logging in if user has signed up."""
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def logout(self, username):
        """Action of logging out if user has logged in."""
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        user.is_logged_in = False
        return False

    def is_logged_in(self, username):
        """Check if user has logged in."""
        if username in self.users:
            return self.users[username].is_logged_in
        return True


class Authorizor:
    '''Class to represent authorization process.

    Attributes:
    ------------
        authenticatorr: Authenticator
            example of class Authenticator
        permissions: dict
            dictionary with users` permissions

    '''

    def __init__(self, authenticatorr):
        """Construct an authorizor to manage
        users usage permissions."""
        self.authenticatorr = authenticatorr
        self.permissions = {}

    def add_permission(self, perm_name):
        """Create a new permission that users
        can be added to"""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """Grant the given permission to the user."""
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticatorr.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        """Check if user is permitted to do some actions."""
        if not self.authenticatorr.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


authenticator = Authenticator()
authorizor = Authorizor(authenticator)
