
class TreeNode(object):

    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class BinaryTree(object):

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
            temp = self.root
            while True:
                if temp.left is None:
                    temp.left = node
                    break
                elif temp.right is None:
                    temp.right = node
                    break
                if self.isNodeFull(temp.left) and not self.isNodeFull(temp.right):
                    temp = temp.right
                else:
                    temp = temp.left

    def insertNode(self, node):
        self.root = node

    def show(self, method="inorder"):
        if method == "inorder":
            traversal = self._inOrderTraversal
        elif method == "preorder":
            traversal = self._preOrderTraversal
        elif method == "postorder":
            traversal = self._postOrderTraversal
        result = []
        result = traversal(self.root, result)
        print("{} traversal:".format(method))
        print([node.val for node in result])

    def _preOrderTraversal(self, rootNode, result=[]):
        if rootNode:
            result.append(rootNode)
            self._preOrderTraversal(rootNode.left, result)
            self._preOrderTraversal(rootNode.right, result)
        return result

    def _postOrderTraversal(self, rootNode, result=[]):
        if rootNode:
            self._postOrderTraversal(rootNode.left, result)
            self._postOrderTraversal(rootNode.right, result)
            result.append(rootNode)
        return result

    def _inOrderTraversal(self, rootNode, result=[]):
        if rootNode:
            self._inOrderTraversal(rootNode.left, result)
            result.append(rootNode)
            self._inOrderTraversal(rootNode.right, result)
        return result


if __name__ == "__main__":
    tree = BinaryTree()
    for idx in range(1, 11):
        tree.insert(idx)
    tree.show()

    # D = TreeNode("D", TreeNode("C"), TreeNode("E"))
    # B = TreeNode("B", TreeNode("A"), D)
    # I = TreeNode("I", TreeNode("H"))
    # G = TreeNode("G", None, I)
    # F = TreeNode("F", B, G)
    # tree.insertNode(F)
    # tree.show("inorder")
    # tree.show("preorder")
    # tree.show("postorder")
