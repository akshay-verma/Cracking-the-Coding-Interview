
class Node(object):

    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

    def __str__(self):
        return self.data


class Stack(object):

    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.nxt = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            raise AssertionError("Stack is empty")
        val = self.top.data
        self.top = self.top.nxt
        return val

    def peek(self):
        return self.top.data if self.top else None

    def __str__(self):
        curr = self.top
        string = ""
        while curr is not None:
            string += "{}".format(curr.data)
            if curr.nxt is not None:
                string += "->"
            curr = curr.nxt
        return string

    def isEmpty(self):
        return self.top is None
