"""
Stack to queue converter.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """
    converts stack to queue
    """
    stack_copy = ArrayStack(stack)
    queue = ArrayQueue()
    while True:
        try:
            element = stack_copy.pop()
            queue.add(element)
        except KeyError:
            break
    queue_reversed = ArrayQueue()
    while True:
        try:
            element = queue.pop()
            queue_reversed.add(element)
        except KeyError:
            break
    return queue_reversed


def main():
    """
    tests the module.
    """
    stack = ArrayStack()
    for i in range(10):
        stack.add(i)
    queue = stack_to_queue(stack)
    assert str(queue) == "[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]"
    assert str(stack) == "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
    assert stack.pop() == 9
    assert queue.pop() == 9
    stack.add(11)
    queue.add(11)
    assert str(queue) == "[8, 7, 6, 5, 4, 3, 2, 1, 0, 11]"
    assert str(stack) == "[0, 1, 2, 3, 4, 5, 6, 7, 8, 11]"
    print("Success!")


if __name__ == "__main__":
    main()
