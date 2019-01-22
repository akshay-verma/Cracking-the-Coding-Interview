"""
3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""

from linked_list import LinkedList


class Stack(object):

    def __init__(self):
        self.list = LinkedList()
        self.curr = None
        self.minVal = None

    def push(self, data):
        self.list.append(data)
        if self.curr is None:
            self.curr = self.list.head
        else:
            self.curr = self.curr.nxt
        if not self.minVal or self.minVal > data:
            self.minVal = data

    def pop(self):
        self.list.delete(self.curr.data)

    def show(self):
        self.list.show()

    @property
    def min(self):
        return self.minVal


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(0)
    stack.show()
    stack.pop()
    stack.show()
    print(stack.min)
