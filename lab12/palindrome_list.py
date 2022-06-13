"""
Palindrome class realization.
"""

from arraystack import ArrayStack

class Palindrome:
    """Class to represent search of palindromes in files."""

    def read_file(self, path):
        """Reads words from file."""
        # words = []
        with open(path, "r") as file:
            lines = [line.strip().split()[0] for line in file.readlines()]
            # words = [el for line in lines for el in line]
        return lines

    def find_palindromes(self, path_to_read, path_to_save):
        """Find palindromes in file, write them to new file."""
        words = self.read_file(path_to_read)
        palindromes = []
        for word in words:
            stack = ArrayStack()
            reversed_string = ""
            for el in word:
                stack.push(el)
            while not stack.isEmpty():
                reversed_string += stack.pop()
            if reversed_string.lower() == word.lower():
                palindromes.append(word)
        self.write_to_file(path_to_save, palindromes)
        return palindromes

    def write_to_file(self, path, words):
        """Writes palindromes to new file."""
        with open(path, "w") as file:
            for element in words[:-1]:
                file.write(f"{element}\n")
            file.write(words[-1])

a = Palindrome()
a.find_palindromes("words.txt", "endh.txt")
