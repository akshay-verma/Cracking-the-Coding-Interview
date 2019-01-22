
class Node(object):

    def __init__(self, leaf=False):
        self.values = []
        self.children = []
        self.leaf = leaf

    def findSlot(self, val):
        index = len(self.values) - 1
        while index >= 0 and self.values[index] > val:
            index -= 1
        return index + 1

    def add(self, val):
        index = len(self.values) - 1
        self.values.append(0)
        while index >= 0 and self.values[index] > val:
            self.values[index + 1] = self.values[index]
            index -= 1
        self.values[index + 1] = val

    def __str__(self):
        string = ""
        for val in self.values:
            string += str(val) + ","
        return string

    @property
    def size(self):
        return len(self.values)


class BTree(object):

    def __init__(self, degree):
        self.root = Node(leaf=True)
        self.degree = degree

    @property
    def maxKeys(self):
        return (2 * self.degree) - 1

    @property
    def maxChildren(self):
        return self.maxKeys + 1

    def insertNonFull(self, node, value):
        if node.leaf:
            node.add(value)
        else:
            index = node.findSlot(value)
            if node.children[index].size >= self.maxKeys:
                self.splitFullNode(node, index)
                if value > node.values[index]:
                    index += 1
            self.insertNonFull(node.children[index], value)

    def splitFullNode(self, node, index):
        child = node.children[index]
        rightNode = Node(leaf=child.leaf)

        node.values.insert(index, child.values[self.degree - 1])
        node.children.insert(index + 1, rightNode)

        rightNode.values = child.values[self.degree: self.maxKeys]
        child.values = child.values[0: self.degree - 1]

        if not child.leaf:
            rightNode.children = child.children[self.degree: self.maxChildren]
            child.children = child.children[0: self.degree]

    def insert(self, value):
        rootNode = self.root
        if rootNode.size >= self.maxKeys:
            newRoot = Node()
            self.root = newRoot
            newRoot.children.insert(0, rootNode)
            self.splitFullNode(newRoot, 0)
            self.insertNonFull(newRoot, value)
        else:
            self.insertNonFull(rootNode, value)


if __name__ == "__main__":
    tree = BTree(2)
    for idx in range(1, 10):
        tree.insert(idx)
    print(tree.root)
