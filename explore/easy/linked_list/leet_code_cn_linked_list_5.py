# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp_head = head
        temp_stack = list()
        while temp_head is not None:
            print(temp_head.val)
            temp_stack.append(temp_head.val)
            temp_head = temp_head.next
        while head is not None:
            if head.val != temp_stack.pop():
                return False
            head = head.next

        return True


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(3)
    node4 = ListNode(1)

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
    result = solution.isPalindrome(node1)
    print(result)
