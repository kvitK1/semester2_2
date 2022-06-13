"""module to test validator class"""

from validator import Validator
import unittest


class TestValidator(unittest.TestCase):
    """Class to test Validator class methods.

    Attributes:
        valid: Validator

    """

    valid = Validator()

    def test_name(self):
        """Test validate_name_surname."""
        self.assertTrue(self.valid.validate_name_surname("Elvis Presley"))
        self.assertFalse(self.valid.validate_name_surname("Elvis PResley"))

    def test_age(self):
        """Test validate_age."""
        self.assertTrue(self.valid.validate_age("20"))
        self.assertFalse(self.valid.validate_age("7"))

    def test_country(self):
        """Test validate_country."""
        self.assertTrue(self.valid.validate_country("Ukraine"))
        self.assertFalse(self.valid.validate_country("UUUUkraine"))
        self.assertTrue(self.valid.validate_country("USA"))
        self.assertFalse(self.valid.validate_country("USAb"))

    def test_region(self):
        """Test validate_region."""
        self.assertTrue(self.valid.validate_region("Lviv"))
        self.assertTrue(self.valid.validate_region("Lviv1"))
        self.assertFalse(self.valid.validate_region("lviv"))

    def test_living_place(self):
        """Test validate_living_place."""
        self.assertTrue(self.valid.validate_living_place("Koselnytska st. 2a"))
        self.assertFalse(self.valid.validate_living_place("Koselnytska provulok 2a"))

    def test_index(self):
        """Test index."""
        self.assertTrue(self.valid.validate_index("79000"))
        self.assertFalse(self.valid.validate_index("790"))

    # def test_phone(self):
    #     """Test validate_phone."""
    #     self.assertTrue(self.valid.validate_phone("+380951234567"))
    #     self.assertTrue(self.valid.validate_phone("+38 (095) 123-45-67"))
    #     self.assertFalse(self.valid.validate_phone("38 (095) 123-45-677"))

    # def test_email(self):
    #     """Test validate_email."""
    #     self.assertTrue(self.valid.validate_email("username@domain.com"))
    #     self.assertFalse(self.valid.validate_email("username@domain.aaa"))
    #     self.assertEqual(self.valid.validate_email(".myemail@ukr.net"), False)

    # def test_id(self):
    #     """Test validate_id."""
    #     self.assertTrue(self.valid.validate_id("123450"))
    #     self.assertFalse(self.valid.validate_id("123050"))

    # def test_validate(self):
    #     """Test validate."""
    #     self.assertTrue(self.valid.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"))
    #     self.assertFalse(self.valid.validate("Elvis Presley20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"))

if __name__ == "__main__":
    unittest.main()
