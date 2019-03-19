# Definition for singly-linked list. (GIVEN)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# END GIVEN CODE


class LinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def add_node(self, x):
        if self.first_node is None:
            self.first_node = ListNode(x)
            self.last_node = self.first_node
        else:
            self.last_node.next = ListNode(x)
            self.last_node = self.last_node.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = '', ''

        num1 = str(l1.val) + num1
        while l1.next is not None:
            l1 = l1.next
            num1 = str(l1.val) + num1
        num2 = str(l2.val) + num2
        while l2.next is not None:
            l2 = l2.next
            num2 = str(l2.val) + num2

        result = reversed(str(int(num1) + int(num2)))
        result_list = LinkedList()
        for d in result:
            result_list.add_node(int(d))

        return result_list.first_node
