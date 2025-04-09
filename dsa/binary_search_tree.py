class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __repr__(self):
        return str(self.data)

class BinarySearchTree:
    root: Node | None = None

    def __init__(self):
        self.root = None

    def add(self, new_node: Node):
        print("add node:", new_node)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while current_node:
            if new_node == current_node:
                raise ValueError("Binary search tree cannot have duplicate nodes")
            elif new_node < current_node:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
        self.print_tree_vertical()

    def remove(self, key: int):
        print("remove node:", key)
        parrent_node = None
        current_node = self.root

        while current_node:
            if key == current_node.data:
                if current_node.left is None and current_node.right is None:
                    removed_node_replaced_by = None
                    if current_node < parrent_node:
                        parrent_node.left = removed_node_replaced_by
                    else:
                        parrent_node.right = removed_node_replaced_by
                elif current_node.left is not None and current_node.right is not None:
                    # Use successor node ro replace removed node
                    semi_successor = None
                    successor = current_node.right
                    while successor.left is not None:
                        semi_successor = successor
                        successor = successor.left

                    current_node.data = successor.data
                    if semi_successor is not None:
                        semi_successor.left = None
                    else:
                        current_node.right = successor.right

                else:
                    removed_node_replaced_by = current_node.left if current_node.left is not None else current_node.right

                    if current_node < parrent_node:
                        parrent_node.left = removed_node_replaced_by
                    else:
                        parrent_node.right = removed_node_replaced_by

                break
            elif key < current_node.data:
                if current_node.left is not None:
                    parrent_node = current_node
                    current_node = current_node.left
                else:
                    return print("Search result: Key not found", key)
            else:
                if current_node.right is not None:
                    parrent_node = current_node
                    current_node = current_node.right
                else:
                    return print("Search result: Key not found", key)
        self.print_tree_vertical()

    def search(self, key):
        current_node = self.root

        while current_node:
            if key == current_node.data:
                print("Search result: Key found", key)
                return current_node
            elif key < current_node.data:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    return print("Search result: Key not found", key)
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    return print("Search result: Key not found", key)

    def print_tree_vertical(self):
        """
        Prints the binary tree vertically (top-down representation).
        This is more complex but provides a traditional tree view.
        """
        root = self.root
        if not root:
            print("Empty tree")
            return

        # Calculate the height of the tree
        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

        h = height(root)

        # Calculate the width needed for the bottom level
        width = 2 ** h - 1

        # Initialize a 2D grid to represent the tree
        grid = [[" " for _ in range(width)] for _ in range(h)]

        # Fill the grid with tree nodes
        def fill_grid(node: Node, level, left, right):
            if not node:
                return

            mid = (left + right) // 2
            grid[level][mid] = str(node.data)

            # Process left and right children
            fill_grid(node.left, level + 1, left, mid - 1)
            fill_grid(node.right, level + 1, mid + 1, right)

        fill_grid(root, 0, 0, width - 1)

        # Print the grid
        for row in grid:
            print("".join(row))

    def traverse_tree(self, node: Node, level=0):
        left_level = self.traverse_tree(node.left, level + 1) if node.left is not None else level
        right_level = self.traverse_tree(node.right, level + 1) if node.right is not None else level
        return max(left_level, right_level)


tree = BinarySearchTree()
tree.add(Node(10))
tree.add(Node(1))

tree.add(Node(3))
tree.add(Node(5))
tree.add(Node(8))
tree.add(Node(9))
tree.add(Node(7))
tree.add(Node(4))
tree.add(Node(2))
tree.add(Node(0))
tree.add(Node(15))
tree.add(Node(13))
tree.add(Node(14))
tree.add(Node(18))
tree.add(Node(19))
tree.add(Node(17))
tree.add(Node(11))
tree.add(Node(12))

tree.remove(5)
tree.remove(7)
tree.remove(3)
tree.remove(13)
tree.remove(18)
tree.remove(4)
