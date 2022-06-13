"""validator task"""

import re


class Validator:
    """Class to validate inforamtion about person."""

    def validate_name_surname(self, name):
        """Validates name and surname."""
        name_pattern = r"[A-Z][a-z]{1,29}"
        pattern = f"^{name_pattern} {name_pattern}$"
        return re.match(pattern, name) is not None

    def validate_age(self, age):
        """Validates age."""
        age_pattern1 = r"^1[6-9]$"
        age_pattern2 = r"^[2-9][0-9]$"
        pattern = f"{age_pattern1}|{age_pattern2}"
        return re.match(pattern, age) is not None

    def validate_country(self, country):
        """Validates country."""
        pattern = r"^[A-Z]{2,10}$"
        res = re.match(pattern, country)
        if res is not None:
            return res is not None
        else:
            pattern = r"^[A-Z][a-z]{1,9}$"
            return re.match(pattern, country) is not None

    def validate_region(self, region):
        """Validates region."""
        pattern = r"^[A-Z][a-zA-Z0-9]{1,9}$"
        return re.match(pattern, region) is not None

    def validate_living_place(self, place):
        """Validates living place."""
        street = r"[A-Z][a-z]{2,19}\s((st.\s)|(av.\s)|(prosp.\s)|(rd.\s))[\d][a-z0-9]$"
        return re.match(street, place) is not None

    def validate_index(self, index):
        """Validates index."""
        pattern = r"\d{5}$"
        return re.match(pattern, index) is not None

    def validate_phone(self, phone):
        """Validates phone."""
        pattern1 = r"\+[0-9]{9,12}$"
        pattern2 = r"\+[0-9]{1,2}\s\(\d{3}\)\s\d{2,3}-\d{2,3}-\d{2,3}"
        if re.match(pattern1, phone) is not None:
            return re.match(pattern1, phone) is not None
        if re.match(pattern2, phone) is not None:
            return re.match(pattern2, phone) is not None
        return False

    def validate_email(self, email):
        """Validates email."""
        characters = "! # $ % & ' * + - / = ? ^ _ ` { | } ~ .".split()
        doggy = email.find("@")
        if email[0] == "." or email[doggy-1] == ".":
            return False
        for i in range(1, len(list(email[:doggy]))):
            if list(email[:doggy])[i] == list(email[:doggy])[i-1] and list(email[:doggy])[i] in characters:
                return False
        pattern = r"[\w\d!#$%&'*+-/=?^_`{|}.~]{1,64}@[a-z]{1,255}(\.(gov|ua|net|gmail|org|edu|com))+"
        return re.match(pattern, email) is not None

    def validate_id(self, id_num):
        """Validates id."""
        zeros = id_num.count("0")
        if zeros != 1:
            return False
        else:
            pattern = r"\d{6}$"
            return re.match(pattern, id_num) is not None

    def validate(self, info):
        """Validates all the info."""
        coma = info.find(",") != -1
        dot_coma = info.find(";") != -1
        if coma: 
            info = info.split(",")
        elif dot_coma:
            info = info.split(";")
        else:
            return False
        if len(info) != 9:
            return False

        bol = True
        actions = [self.validate_name_surname, self.validate_age,
        self.validate_country, self.validate_region, self.validate_living_place,
        self.validate_index, self.validate_phone, self.validate_email, self.validate_id]
        for i in range(len(actions)):
            bol = actions[i](info[i].strip())
            if bol is False:
                break
        return bol

valid = Validator()

# def tests():
#     # name and surname
#     assert valid.validate_name_surname("Elvis Presley") is True
#     # Not 2 words
#     assert valid.validate_name_surname("ElvisPresley") is False
#     assert valid.validate_name_surname("Elvis Presley forever") is False

#     # should be only first uppercase letter in name and surname
#     assert valid.validate_name_surname("elvis Presley") is False
#     assert valid.validate_name_surname("Elvis presley") is False
#     assert valid.validate_name_surname("Elvis PResley") is False

#     # size of both name and surname shoulb be between 2 and 30
#     assert valid.validate_name_surname("Elvis Presleyqqqqqqqqqqqqqqqq\
# qqqqqqqqqqqqqqqqqqqqqqq") is False
#     assert valid.validate_name_surname("Elvis P") is False

#     #no digits or punctuation in name or surname
#     assert valid.validate_name_surname("Elvis P,resley") is False
#     assert valid.validate_name_surname("El1vis Presley") is False

#     # valid age id digit berween 16 and 99
#     # assert valid.validate_age("20") is True
#     # assert valid.validate_age("7") is False
#     # assert valid.validate_age("100") is False
#     # assert valid.validate_age("20.") is False
#     # assert valid.validate_age("20a") is False
#     # assert valid.validate_age("12") is False
#     # assert valid.validate_age("99") is True

#     # # valid country - between 2 and 10 chars, first letter should be uppercase,
#     # # can`t contain numbers
#     # assert valid.validate_country("Ukraine") is True
#     # assert valid.validate_country("U") is False
#     # assert valid.validate_country("UUUUUUUUUUUUUUUUUUUUUUU") is False
#     # assert valid.validate_country("Ukraine1") is False
#     # assert valid.validate_country("ukraine") is False
#     # assert valid.validate_country("USA") is True
#     # assert valid.validate_country("USAb") is False

#     # # valid region - the same as country, but can contain numbers
#     # assert valid.validate_region("Lviv") is True
#     # assert valid.validate_region("Lviv1") is True
#     # assert valid.validate_region("L") is False
#     # assert valid.validate_region("lviv") is False

#     # living place - should be in format: "Koselnytska st. 2a"
#     # name of street - between 3 and 20 chars, first character uppercase, no digits in it
#     # type of street - should be "st.", "av.", "prosp." or "rd."
#     # number of building - exactly 2 symbols, first should be number,
#     # second can be number or small letter
#     assert valid.validate_living_place("Koselnytska st. 2a") is True
#     # assert valid.validate_living_place("koselnytska st. 2a") is False
#     # assert valid.validate_living_place("Koselnytska provulok 2a") is False
#     # assert valid.validate_living_place("Koselnytska st. 2") is False
#     # assert valid.validate_living_place("Koselnytska st. a2") is False
#     # assert valid.validate_living_place("Koselnytska st. 22") is True
#     # assert valid.validate_living_place("Koselnytska av. 42") is True
#     # assert valid.validate_living_place("Koselnytska prosp. 4c") is True
#     # assert valid.validate_living_place("Koselnytska st. 123") is False

#     # valid index - exactly 5 digits
#     assert valid.validate_index("79000") is True
#     assert valid.validate_index("7900") is False
#     assert valid.validate_index("790000") is False
#     assert valid.validate_index("7900q") is False
#     assert valid.validate_index("790 00") is False

#     # # valid phone - in format "+380951234567" or "+38 (095) 123-45-67"
#     # # starts wit "+" and has from 9 to 12 numbers
#     assert valid.validate_phone("+380951234567") is True
#     assert valid.validate_phone("+38 (095) 123-45-67") is True
#     assert valid.validate_phone("38 (095) 123-45-67") is False
#     assert valid.validate_phone("380951234567") is False
#     assert valid.validate_phone("-380951234567") is False
#     assert valid.validate_phone("+3810951234567") is False
#     assert valid.validate_phone("+20951234567") is True

#     # valid email should be in format "username@domain.type"
#     # username - any letters, digits, any of "!#$%&'*+-/=?^_`{|}~",
#     # dots (provided that it is not the first or last
#     # character and provided also that it does not appear consecutively), at least 1, at most 64
#     # domain - only lowercase letters, at least 1, at most 255, but
#     # be careful - can be also "." - for example @ucu.edu.ua
#     # type : "com", "org", "edu", "gov", "net", "ua",....
#     assert valid.validate_email("username@domain.com") is True
#     assert valid.validate_email("username+usersurname@domain.com") is True
#     assert valid.validate_email("username@ucu.edu.ua") is True
#     assert valid.validate_email("usernamedomain.com") is False
#     assert valid.validate_email("username@domaincom") is False
#     assert valid.validate_email("username@domain.aaa") is False
#     assert valid.validate_email("username@aaa") is False
#     assert valid.validate_email("@domain.com") is False
#     assert valid.validate_email("my..email@ukr.net") is False
#     assert valid.validate_email(".myemail@ukr.net") is False
#     assert valid.validate_email("myemail.@ukr.net") is False
#     assert valid.validate_email("name.surname.fathername@google.gmail.ucu.edu.ua.com") is True

#     # valid id - exactly 6 digits, but should contain exactly one zero - at any position
#     assert valid.validate_id("123450") is True
#     assert valid.validate_id("011111") is True
#     assert valid.validate_id("123456") is False
#     assert valid.validate_id("123006") is False
#     assert valid.validate_id("1230916") is False
#     assert valid.validate_id("12306") is False

#     # data - string in format "name_surname,age,country,region,living_place,index,phone,email,id"
#     # can also be whitespaces between sections and allowed separator ші ";"
#     # all previous criteria are valid
#     assert valid.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450") is True
#     assert valid.validate("Elvis Presley;20;Ukraine;Lviv;Koselnytska st. 2a;79000;+380951234567;username@domain.com;123450") is True
#     assert valid.validate("Elvis Presley; 20; Ukraine; Lviv; Koselnytska st. 2a; 79000; +380951234567; username@domain.com; 123450") is True
#     assert valid.validate("Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450") is True
#     assert valid.validate("20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450") is False
#     assert valid.validate("Elvis Presley:20,Ukraine&Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450") is False

#     print("done")
# if __name__ == '__main__':
#     tests()