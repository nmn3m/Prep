class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # insert & _insert_recursive
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)

    def in_order_traversal(self, node, visited=None):
        if visited is None:
            visited = []

        if node:
            self.in_order_traversal(node.left, visited)
            visited.append(node.value)
            self.in_order_traversal(node.right, visited)
        return visited

    def pre_order_traversal(self, node, visited=None):
        if visited is None:
            visited = []
        if node:
            visited.append(node.value)
            self.pre_order_traversal(node.left, visited)
            self.pre_order_traversal(node.right, visited)
        return visited

    def post_order_traversal(self, node, visited=None):
        if visited is None:
            visited = []
        if node:
            self.pre_order_traversal(node.left, visited)
            self.pre_order_traversal(node.right, visited)
            visited.append(node.value)
        return visited


bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(2)
bt.insert(7)

print("In-order traversal:", bt.in_order_traversal(bt.root))
print("Pre-order traversal:", bt.pre_order_traversal(bt.root))
print("Post-order traversal:", bt.post_order_traversal(bt.root))
print("Searching for 7:", bt.search(7))
print("Searching for 20:", bt.search(20))
