"""
Stack to queue converter.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """Creates queue from stack."""
    queue = ArrayQueue()
    lst = []
    for element in stack:
        lst.append(element)
    for elem in lst[::-1]:
        queue.add(elem)
    return queue

# s = ArrayStack()
# for i in range(10):
#     s.add(i)
# l = stack_to_queue(s)
# print(s)
# print(l)
# print(s.pop())
# print(l.pop())
# s.add(11)
# l.add(11)
# print(l)
# print(s)
