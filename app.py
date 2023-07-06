import argparse
from search import breadth_first, depth_first, binary


def main():
    parser = argparse.ArgumentParser(description="Search for word in file")

    parser.add_argument("-w", "--word", required=True, help="word to be searched")
    parser.add_argument(
        "-f", "--file", required=True, help="path to file to search through"
    )
    parser.add_argument(
        "-sa",
        "--search-algorithm",
        choices=["binary-search", "depth-first-search", "breadth-first-search"],
        required=True,
        help="algorithm to be use for searching",
    )
    parser.add_argument(
        "-o",
        "--order",
        choices=["pre-order", "post-order", "level-order", "in-order"],
        required=True,
        help="order of traversal",
    )
    args = parser.parse_args()

    # Depth First Search
    if args.search_algorithm == "depth-first-search":
        depth_first.search(args)
        return

    # Breadth First Search
    if args.search_algorithm == "breadth-first-search":
        breadth_first.search(args)
        return

    # Binary Search
    if args.search_algorithm == "binary-search":
        binary.search(args)
        return


if __name__ == "__main__":
    main()
