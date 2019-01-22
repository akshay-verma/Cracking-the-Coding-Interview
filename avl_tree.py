

class AVLNode(object):

    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.balance = 0
        self.val = value
        self.height = 0


class AVLTree(object):

    def __init__(self):
        self.root = None

    def insert(self, obj):
        if type(obj) is AVLNode:
            node = obj
        else:
            node = AVLNode(obj)
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            while True:
                if node.val <= curr.val:
                    if curr.left is None:
                        curr.left = node
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = node
                        break
                    curr = curr.right
            self.rebalance(curr)

    def rotateLeft(self, rotNode):
        newNode = rotNode.right
        rotNode.right = newNode.left
        newNode.left = rotNode
        self.balanceHeight(newNode)
        self.balanceHeight(rotNode)

    def rotateRight(self, rotNode):
        newNode = rotNode.left
        rotNode.left = newNode.right
        newNode.right = rotNode
        self.balanceHeight(rotNode)
        self.balanceHeight(newNode)

    def getHeight(self, node):
        if node:
            return node.height
        return 0

    def balanceHeight(self, node):
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1

    def balanceFactor(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rebalance(self, rotNode):
        self.balanceHeight(rotNode)
        if self.balanceFactor(rotNode) == -2:
            self.rotateLeft(rotNode)

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
        return [node for node in result]

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
    avl = AVLTree()
    dataList = [4, 2, 6, 8, 10]
    for data in dataList:
        avl.insert(data)
    nodes = avl.show()
    for node in nodes:
        print(node.val, node.height)
