# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        index = head
        for i in range(n):
            temp = temp.next
        # 针对需要移除的恰好是链表的第一个元素做特殊处理
        if temp is None:
            head = head.next
            return head

        while temp.next is not None:
            index = index.next
            temp = temp.next

        index.next = index.next.next
        return head


if __name__ == '__main__':
    node1 = ListNode(4)
    # node2 = ListNode(5)
    # node3 = ListNode(1)
    # node4 = ListNode(9)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    solution = Solution()
    result = solution.removeNthFromEnd(node1, 1)
    print(result)
