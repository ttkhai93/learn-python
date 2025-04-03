from collections import deque

class Queue:
    _nodes: deque

    def __init__(self):
        self._nodes = deque()

    def __repr__(self):
        return repr(self._nodes)

    def push(self, element):
        self._nodes.append(element)

    def pop(self):
        return self._nodes.popleft()

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue)

first_value = queue.pop()
print(first_value, queue)

second_value = queue.pop()
print(second_value,queue)