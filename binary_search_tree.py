
class TreeNode(object):

    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def isNodeFull(self, node):
        if node.left and node.right:
            return True
        return False

    def insert(self, val):
        node = TreeNode(val)
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            while True:
                if val <= curr.val:
                    if curr.left is None:
                        curr.left = node
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = node
                        break
                    curr = curr.right

    def show(self):
        result = []
        result = self._inOrderTraversal(self.root, result)
        print([node.val for node in result])

    def _inOrderTraversal(self, rootNode, result=[]):
        if rootNode:
            self._inOrderTraversal(rootNode.left, result)
            result.append(rootNode)
            self._inOrderTraversal(rootNode.right, result)
        return result


if __name__ == "__main__":
    tree = BinarySearchTree()
    inputList = [10, 5, 12, 4, 6, 11, 13]
    for val in inputList:
        tree.insert(val)
    tree.show()
