class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLeft(root):
    if root.left is not None:
        return amountDigits(root.left)


def amountDigits(root):
    global digits
    if root:
        data = root.data
        digits = digits + sum(c.isdigit() for c in data)
        amountDigits(root.left)
        amountDigits(root.right)
    return digits


def getLevelUtil(node, data, level):
    if node is None:
        return 0
    if node.data == data:
        return level
    downlevel = getLevelUtil(node.left,
                             data, level + 1)
    if downlevel != 0:
        return downlevel
    downlevel = getLevelUtil(node.right,
                             data, level + 1)
    return downlevel


def getLevel(node, data):
    return getLevelUtil(node, data, 1)


def convert(root):
    if root is None:
        return
    convert(root.left)
    convert(root.right)
    if root.left is None:
        root.left = root.right
    else:
        root.left.right = root.right
    root.right = None


def downRightTraversal(root):
    if root is not None:
        print(root.data, end=" ")
        downRightTraversal(root.right)
        downRightTraversal(root.left)


def printPreorder(root):
    if root:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)


if __name__ == "__main__":
    digits = 0
    root = Node("Корневой узел")
    root.left = Node("Левый корень поддерева1")
    root.right = Node("Правый корень поддерева")
    root.right.left = Node("Правый левый лист")
    root.right.right = Node("Правый правый лист")
    root.right.right.left = Node("Правый правый левый лист")
    root.left.left = Node("Левый левый лист12")
    root.left.right = Node("Левый правый лист")
    root.left.right.right = Node("Левый правый правый лист")
    print("Tree is: \n")
    printPreorder(root)
    print("\nAmount of digits in left subtree: ", getLeft(root))
    print(f"Level of number is: {getLevel(root, data='Левый левый лист12')}\n")
    print("Vertical form of binary tree: ")
    convert(root)
    downRightTraversal(root)
