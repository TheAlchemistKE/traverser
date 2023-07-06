from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def search(args):
    bt = BinaryTree()

    print("building binary tree...")
    bt.create_from_file(args.file)
    print("Tree Built.")

    if args.order == "level-order":
        print("Searching tree...")
        target = args.word

        if bt.root.value == target:
            print("word found")
            return

        queue = Queue()
        queue.enqueue(bt.root)

        while queue.get_len():
            node = queue.dequeue()

            if node.left:
                if node.left.value == target:
                    print("word found")
                    return
                else:
                    queue.enqueue(node.left)

            if node.right:
                if node.right.value == target:
                    print("word found")
                    return
                else:
                    queue.enqueue(node.right)

        print("word not found")
        return
    print("breadth-first-search only supports --order 'level-order'")
