from decorators import timer
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# solution 1
@timer
def is_palindrome(head: ListNode) -> bool:
    q: List = []

    if not head:
        return True

    node = head
    # list conversion
    while node is not None:
        q.append(node.val)
        node = node.next

    # palindrome validation
    while len(q) > 1:
        if q.pop(0) != q.pop(1):
            return False

    return True


from collections import deque


# solution 2
@timer
def is_palindrome(head: ListNode) -> bool:
    q: deque = deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


# solution 2
@timer
def is_palindrome(head: ListNode) -> bool:
    rev = None  # reverse list
    slow = fast = head

    # create reverse linked list using runner
    while fast and fast.next:
        fast = fast.next.next  # will be None when reached the end
        rev, rev.next, slow = slow, rev, slow.next
    if fast:  # the number of elements in linked-list is odd number
        slow = slow.next  # skipping central elem in case of odd numbered-list
    
    # palindrome validation
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    return not rev  # rev is None when list is palindrome (False)

