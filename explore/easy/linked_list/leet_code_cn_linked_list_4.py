# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        index_a = l1
        index_b = l2
        ans = None
        if index_a.val < index_b.val:
            ans = index_a
            ans.next = self.mergeTwoLists(index_a.next, index_b)
        else:
            ans = index_b
            ans.next = self.mergeTwoLists(index_a, index_b.next)

        return ans


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(5)
    node4 = ListNode(7)
    node5 = ListNode(2)
    node6 = ListNode(3)
    node7 = ListNode(6)
    node8 = ListNode(8)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node5.next = node6
    node6.next = node7
    node7.next = node8
    solution = Solution()
    result = solution.mergeTwoLists(node1, node5)
    print(result)
