"""Node for multiset."""

# A class implementing a node.

class Node:
    """Class to represent Node in multiset.

    Attributes:
    -----------
        item: any value
            info, put in Node
        next: Node|None
            next Node in multiset, default to None
    """

    def __init__(self, item, next = None):
        """
        Produces a newly constructed empty node.
        __init__: Any -> Node
        Fields: item stores any value
            next points to the next node in the list
        """
        self.item = item
        self.next = next

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.item)
