from collections import deque

class Stack:
    _nodes: deque

    def __init__(self):
        self._nodes = deque()

    def __repr__(self):
        return repr(self._nodes)

    def push(self, element):
        self._nodes.append(element)

    def pop(self):
        return self._nodes.pop()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)

first_value = stack.pop()
print(first_value, stack)

second_value = stack.pop()
print(second_value, stack)