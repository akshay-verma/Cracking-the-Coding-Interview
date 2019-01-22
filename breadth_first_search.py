
from binary_tree import BinaryTree, TreeNode

from collections import deque


def breadthFirstSearch(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print("{} ".format(node.val), end="")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print()


def depthFirstSearch(root):
    if root:
        print("{} ".format(root.val), end="")
    if root.left:
        depthFirstSearch(root.left)
    if root.right:
        depthFirstSearch(root.right)


if __name__ == "__main__":
    tree = BinaryTree()
    D = TreeNode("D", TreeNode("C"), TreeNode("E"))
    B = TreeNode("B", TreeNode("A"), D)
    I = TreeNode("I", TreeNode("H"))
    G = TreeNode("G", None, I)
    F = TreeNode("F", B, G)
    tree.insertNode(F)
    print("Breadth First Search...")
    breadthFirstSearch(tree.root)
    print("Depth First Search...")
    depthFirstSearch(tree.root)
