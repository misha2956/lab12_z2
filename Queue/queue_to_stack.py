"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    """
    converts queue to a stack
    """
    queue_copy = ArrayQueue(queue)
    stack = ArrayStack()
    while True:
        try:
            element = queue_copy.pop()
            stack.push(element)
        except KeyError:
            break
    stack_reversed = ArrayStack()
    while True:
        try:
            element = stack.pop()
            stack_reversed.push(element)
        except KeyError:
            break
    return stack_reversed


def main():
    """
    tests module.
    """
    queue = ArrayQueue()
    for i in range(10):
        queue.add(i)
    stack = queue_to_stack(queue)
    assert str(queue) == "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
    assert str(stack) == "[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]"
    assert stack.pop() == 0
    assert queue.pop() == 0
    stack.add(11)
    queue.add(11)
    assert str(queue) == '[1, 2, 3, 4, 5, 6, 7, 8, 9, 11]'
    assert str(stack) == "[9, 8, 7, 6, 5, 4, 3, 2, 1, 11]"
    print("Success!")


if __name__ == "__main__":
    main()
