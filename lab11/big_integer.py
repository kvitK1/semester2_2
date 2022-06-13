"""Lab11 Task3"""


VARIANT = 3

class Node(object):
    """Class to represent Node."""
    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next


class TwoWayNode(Node):
    """Class to represent TwowayNode."""
    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous


class BigInteger:
    """Class to work with large integers in a linked list.
    Attributes:
    -----------
        initValue: "0"|str
            the initial value of number, default to "0"
    """

    def __init__(self, initValue="0"):
        """Construct BigInteger."""
        self.initValue = initValue[1:] if initValue[0] == "-" else initValue
        self.head = self._create_nodes(self.initValue)
        self.positive = initValue[0] != "-"
        self.length = len(initValue if self.positive is True else initValue[1:])

    def __lt__(self, other):
        """Less than."""
        m1 = self.head
        m2 = other.head
        len_m1 = self.length
        len_m2 = other.length
        bol = False
        equ = self.positive == other.positive
        if equ and self.positive is True:
            if len_m1 > len_m2:
                return False
            elif len_m2 > len_m1:
                return True
        elif equ and self.positive is False:
            if len_m1 > len_m2:
                return True
            elif len_m2 > len_m1:
                return False
        elif not equ:
            return False if self.positive else True

        while m1 and m2:
            if m1.data > m2.data:
                if equ and self.positive is True:
                    bol = False
                elif equ and self.positive is False:
                    bol = True
            elif m2.data > m1.data:
                if equ and self.positive is True:
                    bol = True
                elif equ and self.positive is False:
                    bol = False
            m1 = m1.next
            m2 = m2.next
        return bol

    @staticmethod
    def simple_add(bep, other):
        """Simple addition of two numbers."""
        new_poly = BigInteger()
        add1 = bep.head
        add2 = other.head
        previous = None
        head = None
        ost = 0
        while add1 is not None:
            if add2 is not None:
                coef = int(add1.data) + int(add2.data)
                add2 = add2.next
            else:
                coef = int(add1.data)
            if ost == 1:
                coef += 1
                ost = 0

            if coef >= 10:
                if add1.next is None:
                    left = coef
                else:
                    left = coef%10
                head = TwoWayNode(left, previous, head)
                ost = 1
            else:
                head = TwoWayNode(coef, previous, head)
            previous = head
            add1 = add1.next
        new_poly.head = head
        return new_poly

    def __add__(self, rhsint):
        """Addition of two numbers."""
        new_poly = BigInteger()
        if self.positive == rhsint.positive:
            if int(self.initValue) > int(rhsint.initValue):
                new_poly = BigInteger.simple_add(self, rhsint)
            elif int(self.initValue) < int(rhsint.initValue):
                new_poly = BigInteger.simple_add(rhsint, self)
            new_poly.positive = self.positive
        elif self.positive != rhsint.positive:
            if int(self.initValue) > int(rhsint.initValue):
                new_poly = BigInteger.simple_sub(self, rhsint)
                new_poly.positive = self.positive
            elif int(self.initValue) < int(rhsint.initValue):
                new_poly = BigInteger.simple_sub(rhsint, self)
                new_poly.positive = rhsint.positive
        return new_poly

    def __sub__(self, rhsint):
        """Substraction of two numbers."""
        new_poly = BigInteger()
        a = rhsint.positive
        rhsint.positive = not rhsint.positive
        new_poly = self.__add__(rhsint)
        rhsint.positive = a
        return new_poly

    @staticmethod
    def simple_sub(one, other):
        """Simple substraction of two numbers."""
        new_poly = BigInteger()
        add1 = one.head
        add2 = other.head
        previous = None
        head = None
        ost = 0
        while add1:
            if add2 is not None:
                coef = int(add1.data) - int(add2.data)
                add2 = add2.next
            else:
                coef = int(add1.data)
            if ost == 1:
                coef -= 1
                ost = 0
            if coef < 0:
                left = coef+10
                head = TwoWayNode(left, previous, head)
                ost = 1
            else:
               head = TwoWayNode(coef, previous, head)
            previous = head
            add1 = add1.next
        new_poly.head = head
        return new_poly

    def __gt__(self, other):
        """Greater than."""
        mi_1 = self.head
        mi_2 = other.head
        bol = True
        while mi_1 and mi_2:
            if mi_1.data != mi_2.data:
                bol = False
                break
            mi_1 = mi_1.next
            mi_2 = mi_2.next
        if bol:
            return False
        else:
            return not self<other

    def __lshift__(self, rhsint):
        pass

    # def __and__(self, rhsint):
    #     a = bin(int(self.initValue))[2:]
    #     b = bin(int(rhsint.initValue))[2:]
    #     while len(a) != len(b):
    #         b = "0" + b
    #     c = ""
    #     for i in range(len(a)):
    #         temp = int(a[i])&int(b[i])
    #         c += str(temp)
    #     new_bigint = self._create_nodes(c[::-1])
    #     return new_bigint

    def _create_nodes(self, val):
        """Creates numbers as linked list of nodes."""
        head = None
        previous = None
        if val[0] == "-":
            val = val[1:]
        for i in val:
            head = TwoWayNode(i, previous, head)
            previous = head
        return head

    # def binary_to_bigint(self, string):
    #     head = None
    #     previous = None
    #     num = int(string, 2)
    #     while num >= 1:
    #         ost = num%2
    #         head = TwoWayNode(ost, previous, head)
    #         previous = head
    #         num //= 2
    #     return head

    # @staticmethod
    # def bigint_to_binary(head):
    #     start = head
    #     times = 0
    #     nums = 0
    #     while head is not None:
    #         times += 1
    #         head = head.next
    #     head = start
    #     while head is not None:
    #         nums += int(head.data)*(2**(times-1))
    #         times -= 1
    #         head = head.next
    #     bigint = BigInteger._create_nodes(str(nums))
    #     return bigint

    def __str__(self):
        """String representation."""
        string = ""
        current = self.head
        while current is not None:
            string += str(current.data)
            current = current.next
        string = string[1:] if string[0] == "0" and len(string)>1 else string
        string = "-" + string if self.positive is False else string
        return string[::-1]

    def to_string(self):
        """Returns string representation."""
        return str(self)

numa = BigInteger("26")
print(numa)
assert numa.to_string() == "26"
numb = BigInteger("37")
assert numb.head.data == "7"
assert BigInteger("10") == BigInteger("10")
