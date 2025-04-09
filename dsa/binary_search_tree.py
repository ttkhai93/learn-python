class Node:
    def __init__(self, data: int):
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
    root: Node | None

    def __init__(self):
        self.root = None

    def add_node(self, key: int):
        new_node = Node(key)
        print("add node:", new_node)

        if self.root is None:
            self.root = new_node
            return

        self._find_and_append_to_parent_node(new_node, self.root)
        self.print_tree_vertical()


    def _find_and_append_to_parent_node(self, new_node: Node, current_node: Node):
        if new_node == current_node:
            raise ValueError("Binary search tree cannot have duplicate nodes")

        if new_node < current_node:
            if current_node.left is None:
                # If current node doesn't have left child, new node become the left child node
                current_node.left = new_node
            else:
                # If current node already have a left child, continue to traverse to the left side
                self._find_and_append_to_parent_node(new_node, current_node.left)
        else:
            if current_node.right is None:
                # If current node doesn't have right child, new node become the left child node
                current_node.right = new_node
            else:
                # If current node already have a right child, continue to traverse to the right side
                self._find_and_append_to_parent_node(new_node, current_node.right)

    def remove_node(self, key: int):
        print("remove node:", key)
        self._find_and_remove(key, None, self.root)
        self.print_tree_vertical()

    def _find_and_remove(self, key: int, parent_node: Node | None, current_node: Node):
        if key == current_node.data:
            if self._is_leaf_node(current_node):
                if current_node < parent_node:
                    parent_node.left = None
                else:
                    parent_node.right = None
            elif self._is_full_node(current_node):
                successor_node, parent_node = self._find_successor_node(current_node.right)

                # Remove link to successor node
                # If successor node has parent => Remove link from parent to successor node
                if parent_node is not None:
                    parent_node.left = None
                else: # Right child of successor node become right child of the current node
                    current_node.right = successor_node.right

                # Copy successor node data to current node
                current_node.data = successor_node.data
            else:
                child_node = current_node.left if current_node.left is not None else current_node.right
                if current_node < parent_node:
                    parent_node.left = child_node
                else:
                    parent_node.right = child_node
            return

        if key < current_node.data:
            if current_node.left is not None:
                self._find_and_remove(key, current_node, current_node.left)
            else:
                raise ValueError("Key not found:", key)
        else:
            if current_node.right is not None:
                self._find_and_remove(key, current_node, current_node.right)
            else:
                raise ValueError("Key not found:", key)

    def _find_successor_node(self, node: Node, parent_node: Node | None = None):
        if node.left is None:
            return node, parent_node
        else:
            return self._find_successor_node(node.left, node)

    def search(self, key):
        current_node = self.root

        while current_node:
            if key == current_node.data:
                print("Key found", key)
                return current_node
            elif key < current_node.data:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    raise ValueError("Key not found:", key)
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    raise ValueError("Key not found:", key)

    @staticmethod
    def _is_leaf_node(node: Node):
        return node.left is None and node.right is None

    @staticmethod
    def _is_full_node(node: Node):
        return node.left is not None and node.right is not None

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
tree.add_node(10)
tree.add_node(1)
tree.add_node(3)
tree.add_node(5)
tree.add_node(8)
tree.add_node(9)
tree.add_node(7)
tree.add_node(4)
tree.add_node(2)
tree.add_node(0)
tree.add_node(15)
tree.add_node(13)
tree.add_node(14)
tree.add_node(18)
tree.add_node(19)
tree.add_node(17)
tree.add_node(11)
tree.add_node(12)

tree.remove_node(5)
tree.remove_node(7)
tree.remove_node(3)
tree.remove_node(13)
tree.remove_node(18)
tree.remove_node(4)
