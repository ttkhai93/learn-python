from collections import defaultdict
from array import array

class Node:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

    def __lt__(self, other):
        return self.data < other.data

class MinHeap:
    nodes = []

    def push(self, new_node: Node):
        print("push:", new_node)
        self.nodes.append(new_node)

        new_node_pos = len(self.nodes) - 1
        parent_pos = (new_node_pos - 1) // 2

        while parent_pos >= 0:
            if self.nodes[new_node_pos] > self.nodes[parent_pos]:
                break
            print(f"iteration: index={parent_pos}, data={self.nodes[parent_pos]}")

            self.swap_node(new_node_pos, parent_pos)
            new_node_pos = parent_pos
            parent_pos = (new_node_pos - 1) // 2

        self.is_complete_binary_tree()

    def remove(self):
        print("remove")
        self.nodes[0] = self.nodes[-1]
        self.nodes.pop()

        parent_pos = 0
        target_child_pos = self.get_target_child_pos(parent_pos)

        while target_child_pos:
            print(f"iteration: index={parent_pos}, data={self.nodes[parent_pos]}")
            if self.nodes[parent_pos] > self.nodes[target_child_pos]:
                self.swap_node(parent_pos, target_child_pos)
                parent_pos = target_child_pos
                target_child_pos = self.get_target_child_pos(parent_pos)
            else:
                break

        self.is_complete_binary_tree()

    def get_target_child_pos(self, parent_pos) -> int | None:
        left_child_pos = parent_pos * 2 + 1
        right_child_pos = parent_pos * 2 + 2

        # If parent node doesn't have 2 child nodes
        if right_child_pos >= len(self.nodes):
            if left_child_pos >= len(self.nodes):
                return None
            else:
                return left_child_pos
        else:
            if self.nodes[left_child_pos] < self.nodes[right_child_pos]:
                return left_child_pos
            else:
                return right_child_pos

    def parent_node_pos(self, pos: int):
        return (pos-1) // 2

    def swap_node(self, pos: int, new_pos: int):
        print(f"=> swap {self.nodes[pos].data} and {self.nodes[new_pos].data}")
        self.nodes[pos], self.nodes[new_pos] = self.nodes[new_pos], self.nodes[pos]

    def is_complete_binary_tree(self):
        for i in range(len(self.nodes) - 1, 0, -1):
            if self.nodes[i] < self.nodes[self.parent_node_pos(i)]:
                raise ValueError("Tree is invalid", self.nodes)
        print("=> Tree is complete")
        self.print_tree()
        print("--------------------------------")

    def print_tree(self):
        nodes_by_level = defaultdict(list)
        level = 0
        remaining_nodes = len(self.nodes)

        while remaining_nodes > 0:
            max_nodes_in_level = pow(2, level)
            start = pow(2, level) - 1
            end = start + max_nodes_in_level
            for i in range(start, end):
                if i >= len(self.nodes):
                    break
                nodes_by_level[level].append(self.nodes[i].data)

            remaining_nodes -= max_nodes_in_level
            level += 1

        height = level

        for current_level in range(height):
            nodes_in_this_level = nodes_by_level[current_level]
            position = pow(2, height - current_level - 1) - 1
            spacing = pow(2, (height - current_level)) - 1

            # Print leading position
            print(" " * position, end="")

            # Print nodes with spacing
            for i, node in enumerate(nodes_in_this_level):
                print(str(node), end="")
                if i < len(nodes_in_this_level) - 1:
                    print(" " * spacing, end="")

            print()  # New line after each level

    def __repr__(self):
        return str(self.nodes)

heap = MinHeap()
for i in range(9, -1, -1):
    heap.push(Node(i))

heap.remove()
heap.remove()
heap.remove()
heap.remove()
heap.push(Node(3))
heap.push(Node(1))
