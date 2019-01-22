
from collections import deque


class TreeNode(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MinHeap(object):

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
            parentQ = deque()
            curr = self.root
            while True:
                parentQ.append(curr)
                if curr.left is None:
                    curr.left = node
                    break
                if curr.right is None:
                    curr.right = node
                    break
                if self.isNodeFull(curr.left) and not self.isNodeFull(curr.right):
                    curr = curr.right
                else:
                    curr = curr.left
            self.siftUp(parentQ)

    def siftUp(self, parentQ):
        while parentQ:
            parent = parentQ.pop()
            child = None
            if parent.left and parent.left.val < parent.val:
                child = parent.left
            if parent.right and parent.right.val < parent.val:
                child = parent.right
            if child:
                temp = parent.val
                parent.val = child.val
                child.val = temp

    def popLastNode(self):
        nodeQ = deque()
        nodeQ.append(self.root)
        prevNode = None
        while True:
            if not nodeQ:
                if prevNode:
                    if self.isNodeFull(prevNode):
                        prevNode.right = None
                    else:
                        prevNode.left = None
                break
            lastNode = nodeQ.popleft()
            if lastNode.left:
                nodeQ.append(lastNode.left)
            if lastNode.right:
                nodeQ.append(lastNode.right)
            if lastNode.left or lastNode.right:
                prevNode = lastNode
        return lastNode

    def delMin(self):
        if self.root.left and self.root.right:
            lastNode = self.popLastNode()
            self.root.val = lastNode.val
            curr = self.root
        else:
            self.root = None
            return
        while True:
            child = None
            if curr.left is None and curr.right is None:
                break
            if self.isNodeFull(curr):
                if curr.val < curr.left.val and curr.val < curr.right.val:
                    break
                if curr.left.val < curr.right.val:
                    child = curr.left
                else:
                    child = curr.right
            elif curr.left and curr.left.val < curr.val:
                child = curr.left
            else:
                child = curr.right
            if child:
                temp = curr.val
                curr.val = child.val
                child.val = temp
                curr = child
            else:
                break

    def siftDown(self):
        pass

    def show(self, method="inorder"):
        if method == "inorder":
            traversal = self._inOrderTraversal
        elif method == "preorder":
            traversal = self._preOrderTraversal
        elif method == "postorder":
            traversal = self._postOrderTraversal
        result = []
        result = traversal(self.root, result)
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
    minHeap = MinHeap()
    dataList = [4, 6, 2, 10, 12, 14, 16, 1]
    # dataList = [16, 12, 14]
    for data in dataList:
        minHeap.insert(data)
    minHeap.show()
    for data in dataList:
        minHeap.delMin()
        # minHeap.show()
        print("{} ".format(minHeap.root.val), end="")
        # print()
        # break
