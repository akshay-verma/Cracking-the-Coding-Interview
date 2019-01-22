
from linked_list import LinkedList, Node


def removeDuplicates(linkedList):
    """
    Page 94 - Cracking the Coding Interview

    2.1 Remove duplicates: Write code to remove duplicates from an unsorted linked list.
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?
    """
    data = {}
    curr = linkedList.head
    if curr != None:
        data[curr.data] = 1
        while curr.nxt != None:
            if curr.nxt.data not in data:
                data[curr.nxt.data] = 1
                curr = curr.nxt
            else:
                data[curr.nxt.data] += 1
                curr.nxt = curr.nxt.nxt
    return linkedList


def findKthElementFromLast(linkedList, index):
    """
    Page 94 - Cracking the Coding Interview

    2.2 Return Kth to Last: Implement an algorithm to find the kth to last element
    of a singly linked list.
    """
    if not index or linkedList.head == None:
        return None
    curr1 = linkedList.head
    curr2 = linkedList.head

    for idx in range(1, index):
        if curr2.nxt == None:
            return None
        curr2 = curr2.nxt

    while(curr2.nxt != None):
        curr1 = curr1.nxt
        curr2 = curr2.nxt
    return curr1.data


def deleteMiddleNode(linkList, data):
    """
    Page 94 - Cracking the Coding Interview

    2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
    the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
    that node.
    EXAMPLE
    lnput:the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a ->b->d- >e- >f
    """
    curr = linkList.head
    while(curr != None):
        if curr.data == data:
            curr.data = curr.nxt.data
            curr.nxt = curr.nxt.nxt
            return
        curr = curr.nxt


def partition(linkList, data):
    """
    Page 94 - Cracking the Coding Interview

    2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. If x is contained within the list the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.
    EXAMPLE
    Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    """
    curr = linkList.head
    leftList = LinkedList()
    rightList = LinkedList()
    flag = False
    while(curr != None):
        if curr.data == data and flag is False:
            flag = True
            curr = curr.nxt
            continue
        if curr.data < data:
            leftList.append(curr.data)
        else:
            rightList.append(curr.data)
        curr = curr.nxt

    if not flag:
        raise AssertionError("Partition element: {} not found in linked list".format(data))
    leftList.show()
    rightList.show()
    linkList = LinkedList()
    curr = leftList.head
    while(curr != None):
        linkList.append(curr.data)
        curr = curr.nxt
    linkList.append(data)
    curr = rightList.head
    while(curr != None):
        linkList.append(curr.data)
        curr = curr.nxt
    return linkList


def sumOfLinkedList(linkList1, linkList2):
    """
    Page 95 - Cracking the Coding Interview

    2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list.
    Write a function that adds the two numbers and returns the sum as a linked list.

    EXAMPLE
    Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
    Output: 2 -> 1 -> 9. That is, 912.
    FOLLOW UP
    Suppose the digits are stored in forward order. Repeat the above problem.
    Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
    Output: 9 -> 1 -> 2. That is, 912.
    """
    curr1 = linkList1.head
    curr2 = linkList2.head
    newLinkList = LinkedList()
    quotient = 0
    while True:
        if curr1 == None or curr2 == None:
            break
        total = curr1.data + curr2.data + quotient
        quotient = total // 10
        remainder = total % 10
        newLinkList.append(remainder)
        curr1 = curr1.nxt
        curr2 = curr2.nxt
    if quotient:
        newLinkList.append(quotient)
    newLinkList.show()


def detectLoop(linkList):
    curr1 = linkList.head
    curr2 = linkList.head.nxt
    while(curr2 != None):
        if curr1.data == curr2.data:
            return True
        curr1 = curr1.nxt
        curr2 = curr2.nxt
    return False


if __name__ == "__main__":
    # linkList = LinkedList([1,2,3,4,5,6,7,8])
    # # linkList = removeDuplicates(linkList)
    # print(findKthElementFromLast(linkList, 0))
    # deleteMiddleNode(linkList, linkList[3])

    # linkList = LinkedList([3, 5, 8, 5, 10, 2, 1])
    # linkList.show()
    # linkList = partition(linkList, 10)
    # linkList.show()
    # linkList1 = LinkedList([7, 7, 6])
    # linkList2 = LinkedList([5, 9, 6])
    # sumOfLinkedList(linkList1, linkList2)
    print(detectLoop(LinkedList([1,2,3,4,5,6,3])))
