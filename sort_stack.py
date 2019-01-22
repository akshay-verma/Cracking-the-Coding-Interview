"""
Page 99: Cracking the Coding Interview

3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
"""

from stack import Stack


def sortStack(st):
    temp = Stack()
    curr = None
    while not st.isEmpty():
        curr = st.pop()
        while (not temp.isEmpty() and curr > temp.peek()):
            val = temp.pop()
            st.push(val)
        temp.push(curr)
    return temp


if __name__ == "__main__":
    st = Stack()
    data = [10, 5, 9, 1, 4, 15, 8]
    for d in data:
        st.push(d)
    print(st)
    st = sortStack(st)
    print(st)
