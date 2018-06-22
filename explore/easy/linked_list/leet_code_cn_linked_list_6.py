# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        node_set = set()
        node_set.add(head)
        while head.next is not None:
            if head.next in node_set:
                return True
            node_set.add(head.next)
            head = head.next

        return False


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(3)
    node4 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node3

    solution = Solution()
    result = solution.hasCycle(node1)
    print(result)
