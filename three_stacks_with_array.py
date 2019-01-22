"""
3.1 Three in One: Describe how you could use a single array to implement three stacks.
"""


class MultiStack(object):

    def __init__(self, noOfStack):
        self.value = [None] * noOfStack * 10
        self.size = [None] * noOfStack
        self.noOfStack = noOfStack

    def push(self, stackNum, value):
        if stackNum >= (self.noOfStack):
            raise IndexError("Invalid stack selected")

        if self.size[stackNum] and self.size[stackNum] >= len(self.value):
            # TODO: Increase the size of the stack in this case
            raise AssertionError("Size of stack exceeded!")

        if self.size[stackNum] is None:
            index = stackNum
        else:
            index = self.size[stackNum] + self.noOfStack
        self.size[stackNum] = index
        self.value[index] = value

    def show(self):
        print(self.value)

    def pop(self, stackNum):
        if stackNum >= (self.noOfStack):
            raise IndexError("Invalid stack selected")

        value = self.value[self.size[stackNum]]
        self.value[self.size[stackNum]] = None
        self.size[stackNum] -= self.noOfStack
        return value


if __name__ == "__main__":
    stack = MultiStack(3)
    for idx in range(3):
        stack.push(idx, 1)
        stack.push(idx, 2)
        stack.push(idx, 3)
    stack.show()
    stack.pop(0)
    stack.show()
    stack.push(0, 3)
    stack.show()
