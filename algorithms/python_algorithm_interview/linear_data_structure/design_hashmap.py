from collections import defaultdict


class ListNode:
    """
    ListNode is used for chaining in hashmap
    """
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = defaultdict(ListNode)  # if nonexistent key is accessed, default will be automatically created

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative
        :param key:
        :param value:
        :return:
        """
        index = key % self.size  # hashing value - modulo

        # node do not exist in the table[index]
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # node exists; linked-list chaining
        # hash collision; find the last chain node having no next node
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value  # update value
                return
            if p.next is None:  # if chained list do not exist, break loop and create new node for chaining
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :param key:
        :return:
        """
        index = key % self.size

        # nonexistent key in hashmap
        if self.table[index].value is None:
            return -1

        # key exists
        # search keys from chained list(same index)
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value if this map contains a mapping for the key
        :param key:
        :return:
        """
        index = key % self.size
        if self.table[index].value is None:
            return

        # key is the first node in index
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # remove linked list node
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next  # re-chaining from prev to the next node of current node to be removed
                return
            prev, p = p, p.next
