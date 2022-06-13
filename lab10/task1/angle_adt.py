"""lab8, task1. angles from Alien"""


class AngleADT:
    """Class to represent specific way of encoding messages to angles,
    using 16-based numbers."""

    def encode_message(self, chars):
        """Encoding message to list of angles.
        Return list of angles.
        >>> print(AngleADT().encode_message("hi!"))
        [135.0, 45.0, -45.0, 67.5, -157.5, -22.5]
        >>> print(AngleADT().encode_message("ОП"))
        [90.0, -67.5, 292.5, -225.0, -67.5, 315.0]
        """
        curr_angle = 0
        angles = []
        for char in chars:
            angle3 = None
            if len(self.convert_to_num(char)) != 2:
                num1, num2, num3 = self.convert_to_num(char)
                angle1, angle2, angle3 = self.convert_num_to_angle(num1),\
                self.convert_num_to_angle(num2),self.convert_num_to_angle(num3)
            else:
                num1, num2 = self.convert_to_num(char)
                angle1, angle2 = self.convert_num_to_angle(num1),\
                    self.convert_num_to_angle(num2)
            if angle1-curr_angle == 0:
                angles.append(360.0)
            else:
                angles.append(angle1-curr_angle)
            curr_angle = angle1
            if angle1 == angle2 or angle2-curr_angle == 0:
                angles.append(360.0)
            else:
                angles.append(angle2-curr_angle)
            curr_angle = angle2
            if angle3 is not None:
                if angle3 == angle2 or angle3-curr_angle == 0:
                    angles.append(360.0)
                else:
                    angles.append(angle3-curr_angle)
                curr_angle = angle3
        return angles

    def convert_to_num(self, char, fill=2):
        """Converts character to list of numbers.
        Return list of lists with numbers,
        taken from characters transformation.
        >>> print(AngleADT().convert_to_num("a"))
        [6, 1]
        >>> print(AngleADT().convert_to_num("Ї"))
        [4, 0, 7]
        """
        encoded = hex(ord(char))[2:]
        encoded = encoded.rjust(fill, "0")
        nums = []
        for element in encoded:
            if element in "abcdef":
                element = ord(element) - ord("a") + 10
            else:
                element = int(element)
            nums.append(element)
        return nums

    def convert_num_to_angle(self, num):
        """Converts number to certain angle in circle, derived by 16 parts.
        >>> print(AngleADT().convert_num_to_angle(5))
        112.5
        >>> print(AngleADT().convert_num_to_angle(14))
        315.0
        """
        return num*22.5
