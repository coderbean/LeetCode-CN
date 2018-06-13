# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    ## 通过迭代的方式来实现
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        temp = head.next
        new_head = head
        head = head.next
        new_head.next = None
        while temp is not None:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp

        return new_head


if __name__ == '__main__':
    node1 = ListNode(4)
    node2 = ListNode(5)
    node3 = ListNode(1)
    node4 = ListNode(9)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    solution = Solution()
    result = solution.reverseList(node1)
    print(result)
