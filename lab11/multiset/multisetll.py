"""lab11 task1"""

from node import Node

# A class implementing Multiset as a linked list.

class Multiset:
    """
    Class to represent multiset.

    Attributes:
    -----------
        head: None|Node
            a Node, default to None

    """
    def __init__(self):
        """
        Produces a newly constructed empty Multiset.

        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.

        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head is None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.

        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """
        Deletes first occurence in multiset.

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        """
        Deletes all nodes and returns values.
        """
        datas = []
        current = self._head
        while current is not None:
            datas.append(current.item)
            current = current.next
        self._head = None
        return datas

    def split_half(self):
        """
        Splits one multiset to two examples.
        """
        if self._head.next is None:
            return None
        m1_size = (len(self)+1)//2
        m2_size = len(self)//2
        current = self._head
        mult1 = Multiset()
        mult2 = Multiset()
        while m1_size > 0:
            mult1.add(current.item)
            current = current.next
            m1_size -= 1
        while m2_size > 0:
            mult2.add(current.item)
            current = current.next
            m2_size -= 1
        return mult1, mult2

    def __len__(self):
        """
        Counts length of multiset.
        """
        counter = 0
        current = self._head
        while current is not None:
            current = current.next
            counter += 1
        return counter

    def extend(self, other):
        """
        Appends one multiset with nodes of other one.

        :param other: example of Multiset class for extending.
        """
        current = other._head
        elements = []
        while current is not None:
            elements.append(current.item)
            current = current.next
        for elem in reversed(elements):
            self.add(elem)
        return self

    def __str__(self):
        """Returns string implementation of object."""
        string = []
        current = self._head
        while current is not None:
            string.append(current.item)
            current = current.next
        return str(string)

if __name__ == "__main__":
    multiset_1 = Multiset()
    multiset_2 = Multiset()
    multiset_1.add('p')
    multiset_1.add('y')
    multiset_1.add('t')
    multiset_2.add('h')
    multiset_2.add('o')
    multiset_2.add('n')
    assert len(multiset_1) == 3
    assert multiset_1.extend(multiset_2).remove_all() ==\
        ['n', 'o', 'h', 't', 'y', 'p']
    assert multiset_1.empty() is True
