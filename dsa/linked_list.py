from itertools import count
from typing import Optional


class Node:
    data: int
    next: Optional["Node"]

    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    head: Node | None = None

    def __init__(self, head: Node = None):
        self.head = head

    def __repr__(self):
        node = self.head
        node_vals = []
        while node:
            node_vals.append(node.data)
            node = node.next
        node_vals.append("None")
        return " -> ".join([str(val)for val in node_vals])

    def append(self, new_node: Node) -> None:
        new_node.next = self.head
        self.head = new_node

    def append_left(self, new_node: Node) -> None:
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def insert_after(self, new_node: Node, pos: int) -> None:
        if pos < 1:
            raise ValueError("pos must be >= 1")

        node = self.head
        for i in count(1):
            if i < pos:
                node = node.next
                continue

            next_node = node.next
            node.next = new_node
            new_node.next = next_node
            break

    def insert_before(self, new_node: Node, pos: int) -> None:
        if pos < 1:
            raise ValueError("pos must be >= 1")

        node = self.head
        for i in count(1):
            if i + 1 < pos:
                node = node.next
                continue

            new_node.next = node.next
            node.next = new_node
            break

    def pop(self):
        semi_last_node = self.head
        while semi_last_node.next:
            if not semi_last_node.next.next:
                break
            semi_last_node = semi_last_node.next
        semi_last_node.next = None

    def remove(self, target_value: int):
        if self.head.data == target_value:
            self.head = self.head.next

        prev_node = None
        node = self.head
        while node:
            if node.data == target_value:
                prev_node.next = node.next

            prev_node = node
            node = node.next

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

linked_list = LinkedList()
linked_list.append_left(Node(2))
linked_list.append_left(Node(1))
linked_list.append_left(Node(3))
linked_list.append_left(Node(8))
linked_list.append(Node(5))
linked_list.append_left(Node(7))
linked_list.append(Node(6))
linked_list.insert_after(Node(8), 1)
linked_list.insert_before(Node(9), 5)
linked_list.remove(6)
linked_list.remove(5)
linked_list.remove(8)
linked_list.pop()
print(linked_list)