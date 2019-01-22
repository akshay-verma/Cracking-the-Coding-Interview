import random
import time
import sys
import argparse

class AVLTree(object):
    def __init__(self):
        self.root = None

    class __Node(object):
        def __init__(self, val):
            self.val = val
            self.right = None
            self.left = None
            self.height = 1

    def __bfactor(self, node):
        return self.__height(node.right) - self.__height(node.left)

    def insertval(self, val):
        self.root = self.__insert(self.root, val)

    def __insert(self, node, val):
        if node == None:
            node = self.__Node(val)
            return node
        if val == node.val:
            raise Exception("val already in tree")

        if (val < node.val):
#           print val, node.val
            node.left = self.__insert(node.left, val)
        else:
            node.right = self.__insert(node.right, val)
        return self.__balance(node)

    def __fixheight(self, node):
        node.height = max(self.__height(node.right), self.__height(node.left)) + 1

    def __height(self, node):
        if node != None:
            return node.height
        else:
            return 0

    def __rotateLeft(self, node):
        p = node.right
        node.right = p.left
        p.left = node
        self.__fixheight(p)
        self.__fixheight(node)
        return p

    def __rotateRight(self, node):
        q = node.left
        node.left = q.right
        q.right = node
        self.__fixheight(node)
        self.__fixheight(q)
        return q

    def __balance(self, node):
        self.__fixheight(node)
        if self.__bfactor(node) == 2:
            if self.__bfactor(node.right) < 0:
                node.right = self.__rotateRight(node.right)
            return self.__rotateLeft(node)

            if self.__bfactor(node) == -2:
                node.left = self.__rotateLeft(node.left)
            return self.__rotateRight(node)
        return node

    def __bfs_sort(self, node, vals_sorted):
        if node == None:
            return
        self.__bfs_sort(node.left, vals_sorted)
        vals_sorted.append((node.val, node.height))
        self.__bfs_sort(node.right, vals_sorted)

    def sorted(self):
        vals_sorted = list()
        self.__bfs_sort(self.root, vals_sorted)
        return vals_sorted

def merge_sort(data):
    def __merge(list1, list2):
        res = list()
        #print list1, list2
        i1 = i2 = 0
        while i1 < len(list1) and i2 < len(list2):
            if list1[i1] < list2[i2]:
                elem = list1[i1]
                i1 += 1
            else:
                elem = list2[i2]
                i2 += 1
            res.append(elem)

        res.extend(list1[i1:])
        res.extend(list2[i2:])
        #print "Result is", res
        return res


    if len(data) == 1:
        return data
    middle = len(data) / 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return __merge(left, right)

def main(argv):
    fill = 'random'
    nElem = 1000
    w = nElem
    q = 0
    n = 10
    # parser = argparse.ArgumentParser(description='Sorting algorithms comparison')
    # parser.add_argument('--fill', metavar='FILL', type=str,
    #                     help='fill for integer list')
    # parser.add_argument('--n', type = int, metavar = 'n',
    #                     help ='Number of elements in list')
    # parser.add_argument('--q', type = int, metavar = 'q',
    #                     help ='Lower bound of element')
    # parser.add_argument('--w', type = int, metavar = 'w',
    #                     help ='Upper bound of element')

    # args = parser.parse_args(argv)
    # print(args)

    numbers = random.sample(range(q,w), n)
    numbers = list(range(1, 10))

    # random.shuffle(numbers)

    # start_time = time.clock()
    # sorted_numbers = merge_sort(numbers)
    # print time.clock() - start_time
    # print sorted_numbers[0], sorted_numbers[-1]

    tree = AVLTree()
    random.shuffle(numbers)

    for i in numbers:
        tree.insertval(i)
        print(tree.root.val, tree.root.height)
    print(tree.sorted())

    from breadth_first_search import breadthFirstSearch
    breadthFirstSearch(tree.root)
    start_time = time.clock()
    nsorted = tree.sorted()
    # print time.clock() - start_time
    # print nsorted[0], nsorted[-1]

if __name__ == "__main__":
    sys.exit(main(sys.argv))
