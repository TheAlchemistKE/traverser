from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def pre_order(target, root):
    if root:
        if root.value == target:
            return True
        if pre_order(target, root.left):
            return True
        if pre_order(target, root.right):
            return True
    return False


def in_order(target, root):
    if root:
        if in_order(target, root.left):
            return True
        if root.value == target:
            return True
        if in_order(target, root.right):
            return True
    return False


def post_order(target, root):
    if root:
        if post_order(target, root.left):
            return True
        if post_order(target, root.right):
            return True
        if root.value == target:
            return True
    return False


def search(args):
    bt = BinaryTree()

    print("Building the Binary Tree...")
    bt.create_from_file(args.file)
    print("Tree built")

    if args.order == "pre-order":
        print("Searching tree...")
        target = args.word

        if pre_order(target, bt.root):
            print("word found")
            return
        else:
            print("word not found")

    if args.order == "in-order":
        print("Searching tree...")
        target = args.word

        if in_order(target, bt.root):
            print("word found")
            return
        else:
            print("word not found")

    if args.order == "post-order":
        print("Searching tree...")
        target = args.word

        if post_order(target, bt.root):
            print("word found")
            return
        else:
            print("word not found")
