"""
File: node.py

Node classes for one-way linked structures and two-way
linked structures.
"""

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

class TwoWayNode(Node):

    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous
    
    def __str__(self):
        return str(self.data)

class Knot:
    """Lightweight, nonpublic
    class for storing a singly linked node.
    """

    __slots__ = "_element", "_next"     # streamline memory usage

    def __init__(self, element, next):  # initialize node’s fields
        self._element = element         # reference to user’s element
        self._next = next               # reference to next node
