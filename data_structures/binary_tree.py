from data_structures.node import Node
from data_structures.queue import Queue


class BinaryTree:
    def __init__(self):
        self.root = None

    def level_order_insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        q = Queue()
        q.enqueue(self.root)

        while q.get_len():
            node = q.dequeue()
            if not node.left:
                node.left = Node(data)
                return
            else:
                q.enqueue(node.left)

            if not node.right:
                node.right = Node(data)
                return
            else:
                q.enqueue(node.right)

    def bst_insert_recursive(self, data, root):
        if int(data) < int(root.value):
            if root.left is None:
                root.left = Node(data)
            else:
                self.bst_insert_recursive(data, root.left)

        if int(data) > int(root.value):
            if root.right is None:
                root.right = Node(data)
            else:
                self.bst_insert_recursive(data, root.right)

    def bst_insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.bst_insert_recursive(data, self.root)

    def create_from_file(self, path):
        with open(path, "r") as content_file:
            for line in content_file:
                trimmed_line = line.strip()
                if trimmed_line is not "":
                    words = trimmed_line.split()
                    for word in words:
                        self.level_order_insert(word)

    def create_bst_from_file(self, path):
        with open(path, "r") as content_file:
            for line in content_file:
                trimmed_line = line.strip()
                if trimmed_line is not "":
                    words = trimmed_line.split()
                    for word in words:
                        self.bst_insert(word)

    def in_order_print(self, root):
        if root:
            self.in_order_print(root.left)
            print(root.value)
            self.in_order_print(root.right)
