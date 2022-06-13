"""lab 10. task 3"""

from io import StringIO
import numpy as np
from PIL import Image, ImageOps
# import matplotlib.pyplot as plt


path = input("Enter path to file: ")
# mypath = '/Users/kvitoslava/Downloads/crying-cat-meme.jpg'

class GrayscsaleImage:
    """Class to represent a grayscale image;
    contains a LZW-algorithm to comress and decompress the image.

    Attributes
    -----------
        image: Image
            a grayscale image
        nrows: int|0
            number of rows/width (default to 0)
        ncols: int|0
            number of columns/height (default to 0)
        pixels: PixelAccess
            pixels' values

    """

    def __init__(self, nrows=0, ncols=0):
        self.image = open_file(path)
        nrows = self.image.size[0]
        ncols = self.image.size[1]
        self._nrows = nrows
        self._ncols = ncols
        self.pixels = self.image_pixels()

    def image_pixels(self):
        """Cretes PixelAccess object with pixels of image."""
        img_pixels = self.image.load()
        return img_pixels

    def width(self):
        """Width of image."""
        return self._nrows

    def height(self):
        """Height of image."""
        return self._ncols

    def clear(self, value):
        """Sets all pixels to certain value."""
        for row in range(self.height()):
            for col in range(self.width()):
                self.setitem(row, col, value)

    def getitem(self, row, col):
        """Returns value of pixel on certain position."""
        if row in range(self.height()) and col in range(self.width()):
            return self.pixels[row, col]

    def setitem(self, row, col, value):
        """Sets value of pixel on certain position."""
        if row in range(self.height()) and col in range(self.width()) and value in range(0,256):
            self.pixels[row, col] = value

    def create_string(self):
        """Creates string for LZW-algorithm of image compression."""
        string = ""
        for i in range(self.height()):
            for j in range(self.width()):
                string += str(int_to_char(self.pixels[j,i]))
        return string

    def create_image(self, plain):
        """Creates list for LZW-algorithm of image decompression."""
        reconstruct = []
        for char in plain:
            reconstruct.append(char_to_int(char))
        for i in range(self.height()*self.width()-len(reconstruct)):
            reconstruct.append(i)
        return reconstruct

    def lzw_compression(self):
        """LZW-algorithm for image compression."""
        image = self.create_string()
        dict_size = 256
        dictionary = {chr(i):i for i in range(dict_size)}
        string = ""
        output = []
        for char in image:
            temp = string + char
            if temp in dictionary:
                string = temp
            else:
                output.append(dictionary[string])
                dictionary[temp] = dict_size
                dict_size += 1
                string = char

        if len(string) is True:
            output.append(dictionary[string])
        return output

    def lzw_decompression(self):
        """LZW-algorithm for image decompression."""
        compressed = self.lzw_compression()
        dict_size = 256
        dictionary = {i: chr(i) for i in range(dict_size)}
        result = StringIO()
        string = chr(compressed.pop(0))
        result.write(string)
        for num in compressed:
            if num in dictionary:
                entry = dictionary[num]
            elif num == dict_size:
                entry = string + string[0]
            result.write(entry)
            dictionary[dict_size] = string + entry[0]
            dict_size += 1
            string = entry
        decompressed = result.getvalue()
        img = self.create_image(decompressed)
        decompressed = np.reshape(img, (self.height(), self.width()))
        return decompressed

def from_file(mypath):
    """Creates example of GrayscaleImage class."""
    image = open_file(mypath)
    ncols = image.size[1]
    nrows = image.size[0]
    obj = GrayscsaleImage(nrows, ncols)
    return obj

def open_file(mypath):
    """Opens image file."""
    try:
        image = Image.open(rf'{mypath}')
        image = ImageOps.grayscale(image)
        return image
    except FileNotFoundError:
        print("There's no such file")
        quit()

def int_to_char(num):
    """Converts integer to ASCII character."""
    return chr(num//10)

def char_to_int(char):
    """Converts ASCII character to integer."""
    return ord(char)*10

# a = from_file(path)
# a.lzw_compression()
# j = a.lzw_decompression()
# def print_pic(img):
#     #gray image
#     imgplot = plt.imshow(img)
#     plt.show()

# print_pic(a.image)
# print_pic(j)
