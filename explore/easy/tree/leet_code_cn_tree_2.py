# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        l = self.mid_trace(root)
        for i in range(1, len(l)):
            if not l[i] > l[i - 1]:
                return False

        return True

    def mid_trace(self, root):
        if root is None:
            return []
        else:
            return self.mid_trace(root.left) + [root.val] + self.mid_trace(root.right)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    result = solution.isValidBST(root)
    print(result)
