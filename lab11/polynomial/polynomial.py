"""lab11 task2"""

# Implementation of the Polynomial ADT using a sorted linked list.

class Polynomial:
    """Class to represent Polynomial.
    Attributes:
    -----------
        poly_head: None|PolyTermNode
            head of polynomial multiset, default to None
    """

    def __init__(self, degree = None, coefficient = None):
        """Create a new polynomial object."""
        if degree is None :
            self._poly_head = None
        else :
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head

    def degree(self):
        """Return the degree of the polynomial."""
        if self._poly_head is None :
            return -1
        else :
            return self._poly_head.degree

    def __getitem__(self, degree):
        """Return the coefficient for the term of the given degree."""
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        cur_node = self._poly_head
        while cur_node is not None and cur_node.degree != degree :
            cur_node = cur_node.next

        if cur_node is None or cur_node.degree != degree :
            return 0.0
        else :
            return cur_node.coefficient

    def evaluate(self, scalar):
        """Evaluate the polynomial at the given scalar value."""
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        cur_node = self._poly_head
        while cur_node is not None :
            result += cur_node.coefficient * (scalar ** cur_node.degree)
            cur_node = cur_node.next
        return result

    def __add__(self, rhs_poly):
        """Polynomial addition: newPoly = self + rhs_poly."""
        new_pol = self.reduce(rhs_poly)
        return new_pol

    def __sub__(self, rhs_poly):
        """Polynomial subtraction: newPoly = self - rhs_poly."""
        new_pol = self.reduce(rhs_poly, reduce=(lambda x, y: x-y))
        return new_pol

    def __mul__(self, rhs_poly):
        """Polynomial multiplication: newPoly = self * rhs_poly."""
        new_poly = Polynomial()
        mset1 = self._poly_head
        mset2 = rhs_poly._poly_head
        while mset1 is not None:
            while  mset2 is not None:
                coef = mset1.coefficient*mset2.coefficient
                degree = mset1.degree + mset2.degree
                new_poly._append_term(degree, coef)
                mset2 = mset2.next
            mset2 = rhs_poly._poly_head
            mset1 = mset1.next
        self.simplify(new_poly)
        return new_poly

    def simplify(self, poly):
        """Simplify polynomial, add coefficients with same degree."""
        simp = poly._poly_head
        new_poly = None
        while simp is not None and simp.next is not None:
            new_poly = simp
            while new_poly.next is not None:
                if simp.degree == new_poly.next.degree:
                    simp.coefficient += new_poly.next.coefficient
                    new_poly.next = new_poly.next.next
                else:
                    new_poly = new_poly.next
            simp = simp.next

    def reduce(self, rhs_poly, reduce=None):
        """Helper-method to add/substract polynomials."""
        reduce = reduce or (lambda x, y: x+y)
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_degree = rhs_poly.degree()

        i = max_degree
        while i >= 0:
            value = reduce(self[i], rhs_poly[i])
            new_poly._append_term(i, value)
            i -= 1
        return new_poly

    def _append_term(self, degree, coefficient):
        """Helper method for appending terms to the polynomial."""
        if coefficient != 0.0:
            new_term =_PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term
            else:
                self._poly_tail.next = new_term
            self._poly_tail = new_term

    def __str__(self):
        """Print polynomial."""
        current = self._poly_head
        string = ""
        while current is not None:
            if current.coefficient < 0:
                string += str(current)
            else:
                string += f"+{str(current)}"
            current = current.next
        if string.startswith("+"):
            string = string[1:]
        return string


class _PolyTermNode(object):
    """Class for creating polynomial term nodes used with the linked list.
    Attributes:
    -----------
        degree: float
            degree of polyterm
        coefficient: float
            coefficient of polyterm
        next: PolyTermNode|None
            next polyterm in linked list polynomial, default to None
    """

    def __init__(self, degree, coefficient):
        """Create new object."""
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.coefficient) + "x" + str(self.degree)
