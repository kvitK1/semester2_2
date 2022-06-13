"""
File: linkedbst.py
Author: Ken Lambert
"""

from math import log
import random
from time import time
from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
# from linkedqueue import LinkedQueue


class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            string = ""
            if node is not None:
                string += recurse(node.right, level + 1)
                string += "| " * level
                string += str(node.data) + "\n"
                string += recurse(node.left, level + 1)
            return string

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        return None

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        return None

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        return None

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) is not None

    def iterative_find(self, item):
        """Find method but iterative."""
        node = self._root
        while True:
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                node = node.left
            else:
                node = node.right

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def iterative_add(self, item):
        """Add method but iterative."""
        if not self.isEmpty():
            node = self._root
            while True:
                if item > node.data:
                    if node.right is None:
                        node.right = BSTNode(item)
                        break
                    else:
                        node = node.right
                else:
                    if node.left is None:
                        node.left = BSTNode(item)
                        break
                    else:
                        node = node.left
        else:
            self._root = BSTNode(item)
        self._size += 1

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left is None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right is None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
                # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            current_node = top.left
            while not current_node.right is None:
                parent = current_node
                current_node = current_node.right
            top.data = current_node.data
            if parent == top:
                top.left = current_node.left
            else:
                parent.right = current_node.left

        # Begin main part of the method
        if self.isEmpty():
            return None

        # Attempt to locate the node containing the item
        item_removed = None
        pre_root = BSTNode(None)
        pre_root.left = self._root
        parent = pre_root
        direction = 'L'
        current_node = self._root
        while not current_node is None:
            if current_node.data == item:
                item_removed = current_node.data
                break
            parent = current_node
            if current_node.data > item:
                direction = 'L'
                current_node = current_node.left
            else:
                direction = 'R'
                current_node = current_node.right

        # Return None if the item is absent
        if item_removed is None:
            return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not current_node.left is None \
                and not current_node.right is None:
            liftMaxInLeftSubtreeToTop(current_node)
        else:

            # Case 2: The node has no left child
            if current_node.left is None:
                new_child = current_node.right

                # Case 3: The node has no right child
            else:
                new_child = current_node.left

                # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = new_child
            else:
                parent.right = new_child

        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = pre_root.left
        return item_removed

    def replace(self, item, new_item):
        """
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe is not None:
            if probe.data == item:
                old_data = probe.data
                probe.data = new_item
                return old_data
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        '''
        Return the height of tree
        :return: int
        '''

        def height1(top):
            '''
            Helper function
            :param top:
            :return:
            '''
            if not top.left and not top.right:
                return 0
            right_sum = height1(top.right) if top.right else 0
            left_sum = height1(top.left) if top.left else 0
            return max(right_sum, left_sum) + 1
        return height1(self._root)

    def is_balanced(self):
        '''
        Return True if tree is balanced
        :return:
        '''
        tree_height = self.height()
        nodes = self._size
        return tree_height < 2*log(nodes+1)-1

    def rangeFind(self, low, high):
        """
        Returns a list of the items in the tree, where low <= item <= high.
        :param low:
        :param high:
        :return:
        """
        nodes = list(self.inorder())
        ranged_items = []
        for node in nodes:
            if low<=node<=high:
                ranged_items.append(node)
        return ranged_items

    def rebalance(self):
        """
        Rebalances the tree.
        :return:
        """
        elements = list(self.inorder())

        def rebalance1(elements):
            if len(elements) == 0:
                return None
            i = len(elements)//2
            node = BSTNode(elements[i])
            node.left = rebalance1(elements[:i])
            node.right = rebalance1(elements[i+1:])
            return node

        self._root = rebalance1(elements)

    def successor(self, item):
        """
        Returns the smallest item that is larger than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        nodes = list(self.inorder())
        for node in nodes:
            if node > item:
                return node

    def predecessor(self, item):
        """
        Returns the largest item that is smaller than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        nodes = list(self.inorder())
        for node in reversed(nodes):
            if node < item:
                return node

    def demo_bst(self, path):
        """
        Demonstration of efficiency binary search tree for the search tasks.
        :param path:
        :type path:
        :return:
        :rtype:
        """
        searching_words = 10000
        words_list = open_file(path)
        tested_words = []
        for _ in range(searching_words):
            tested_words.append(random.choice(words_list))
        list_time0 = time()
        for word in tested_words:
            words_list.index(word)
        list_time1 = time()-list_time0
        print(f"Search time for {searching_words} random words \
in ordered list: {list_time1}")

        ordered_bst = LinkedBST()
        for word in words_list:
            ordered_bst.iterative_add(word)
        ordered_bst_time0 = time()
        for word in tested_words:
            ordered_bst.iterative_find(word)
        ordered_bst_time1 = time()-ordered_bst_time0
        print(f"Search time for {searching_words} random words \
in ordered bst: {ordered_bst_time1}")

        random.shuffle(words_list)
        unordered_bst = LinkedBST()
        for word in words_list:
            unordered_bst.iterative_add(word)
        unordered_bst_time0 = time()
        for word in tested_words:
            unordered_bst.iterative_find(word)
        unordered_bst_time1 = time()-unordered_bst_time0
        print(f"Search time for {searching_words} random words \
in unordered bst: {unordered_bst_time1}")

        unordered_bst.rebalance()
        balanced_bst_time0 = time()
        for word in tested_words:
            unordered_bst.iterative_find(word)
        balanced_bst_time1 = time()-balanced_bst_time0
        print(f"Search time for {searching_words} random words \
in balanced bst: {balanced_bst_time1}")

def open_file(path):
    """Reads file."""
    words_list = []
    try:
        with open(path, "r") as file:
            words_list = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("No such file.")
    return words_list

# if __name__ == "__main__":
#     lbst = LinkedBST()
#     lbst.demo_bst('words.txt')
