"""
Page 99: Cracking the Coding Interview

Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
"""


from stack import Stack


class MyStack(object):

    def __init__(self, threshold, numOfStacks=3):
        self.stackList = []
        for idx in range(numOfStacks):
            self.stackList.append(Stack())
        self.threshold = threshold
        self.stackSize = [0] * numOfStacks
        self.currentStack = 0

    def push(self, value):
        if self.stackSize[self.currentStack] >= self.threshold:
            if (self.currentStack + 1) >= len(self.stackList):
                self.stackList.append(Stack())
                self.stackSize.append(0)
            self.currentStack += 1
        self.stackList[self.currentStack].push(value)
        self.stackSize[self.currentStack] += 1

    def isEmpty(self, stackNum):
        if self.stackList[stackNum].top is None:
            return True
        return False

    def pop(self):
        if self.isEmpty(self.currentStack):
            if self.currentStack == 0:
                raise AssertionError("Stack is empty")
            self.currentStack -= 1
        return self.stackList[self.currentStack].pop()

    def popAt(self, stackNum):
        if stackNum >= 0 and stackNum <= len(self.stackList):
            self.stackList[stackNum].pop()
            return
        raise AssertionError("Invalid stack number selected")

    def __str__(self):
        string = ""
        for idx in range(len(self.stackList)):
            string += "Stack {}: {}\n".format(idx, self.stackList[idx])
        return string


if __name__ == "__main__":
    stack = MyStack(3)
    for idx in range(28):
        stack.push(10)
    print(stack)
