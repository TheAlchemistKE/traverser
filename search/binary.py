from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def binary_search(target, root):
    if root:
        if target == root.value:
            return True

        if int(target) < int(root.value):
            if binary_search(target, root.left):
                return True

        if binary_search(target, root.right):
            return True
    return False


def search(args):
    bst = BinaryTree()
    print("Building Tree")
    bst.create_bst_from_file(args.file)
    print("Tree Built")
    # bst.in_order_print(bst.root)
    print("Searching Tree...")
    target = args.word
    if binary_search(target, bst.root):
        print("word found")
        return
    else:
        print("word not found")
