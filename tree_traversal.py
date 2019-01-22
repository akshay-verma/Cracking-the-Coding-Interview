
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrderTraversal(rootNode, result=[]):
    if rootNode:
        result.append(rootNode)
        preOrderTraversal(rootNode.left)
        preOrderTraversal(rootNode.right)
    return result


def inOrderTraversal(rootNode, result=[]):
    if rootNode:
        inOrderTraversal(rootNode.left)
        result.append(rootNode)
        inOrderTraversal(rootNode.right)
    return result


def postOrderTraversal(rootNode, result=[]):
    if rootNode:
        postOrderTraversal(rootNode.left)
        postOrderTraversal(rootNode.right)
        result.append(rootNode)
    return result


def printTree(order):
    for node in order:
        print("{}->".format(node.val), end="")
    print()


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    preOrder = preOrderTraversal(root)
    print("Pre-order traversal:")
    printTree(preOrder)

    inOrder = inOrderTraversal(root)
    print("In-order traversal:")
    printTree(inOrder)

    postOrder = postOrderTraversal(root)
    print("Post-order traversal:")
    printTree(postOrder)
