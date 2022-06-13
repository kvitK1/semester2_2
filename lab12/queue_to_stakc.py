"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    """Creates queue from stack."""
    stack = ArrayStack()
    lst = []
    for element in queue:
        lst.append(element)
    for elem in lst[::-1]:
        stack.add(elem)
    return stack

# q = ArrayQueue()
# for i in range(10):
#     q.add(i)
# print(q)
# s = queue_to_stack(q)
# print(s)
# print(s.pop())
# print(q.pop())
# s.add(11)
# q.add(11)
# print(q)
# print(s)
