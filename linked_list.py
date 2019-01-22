
class Node(object):

    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt


class LinkedList(object):

    def __init__(self, content=[]):
        self.head = None
        self.length = 0
        for cont in content:
            self.append(cont)

    def append(self, data):
        if self.head is None:
            curr = Node(data)
            self.head = curr
            self.length += 1
            return
        curr = self.head
        while True:
            if curr.nxt is None:
                break
            curr = curr.nxt
        curr.nxt = Node(data)
        self.length += 1

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.nxt
            self.length -= 1
            return
        curr = self.head
        while(curr is not None):
            if curr.nxt.data == data:
                curr.nxt = curr.nxt.nxt
                self.length -= 1
                return
            curr = curr.nxt

    def search(self, data):
        curr = self.head
        while(curr is not None):
            if curr.data == data:
                return curr
            curr = curr.nxt
        return None

    def show(self):
        curr = self.head
        while(curr is not None):
            print("{}".format(curr.data), end="")
            if curr.nxt is not None:
                print("->", end="")
            curr = curr.nxt
        print()

    def __getitem__(self, index):
        if index >= 0 and index < self.length:
            curr = self.head
            for idx in range(index):
                curr = curr.nxt
            return curr.data
        raise IndexError("linked list index({}) out of range".format(index))

    def __setitem__(self, index, value):
        if index >= 0 and index < self.length:
            curr = self.head
            for idx in range(index):
                curr = curr.nxt
            curr.data = value
            return
        raise IndexError("linked list assignment index({}) out of range".format(index))

    def __len__(self):
        return self.length

    def __iter__(self):
        curr = self.head
        while(curr is not None):
            yield curr.data
            curr = curr.nxt

    def __add__(self, list1):
        if type(list1) is not type(self):
            raise AssertionError("Type mismatch, cannot be concatenated")

        result = LinkedList()
        for item in self:
            result.append(item)

        for item in list1:
            result.append(item)

        return result

    def __eq__(self, list1):
        if len(self) != len(list1):
            return False

        if type(self) != type(list1):
            return False

        curr1 = self.head
        curr2 = list1.head
        for idx in range(len(list1)):
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.nxt
            curr2 = curr2.nxt
        return True

    def __contains__(self, data):
        for item in self:
            if item == data:
                return True
        return False
