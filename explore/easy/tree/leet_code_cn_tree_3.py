# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 解题思路：将先序遍历和中序遍历保存，反转这棵树，重新计算先序遍历和中序遍历，如果先后相同，则为对称二叉树。
# tip：先序和中序遍历可以确定一棵树
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        middle_list_before = self.left_middle_right_trace(root)
        first_list_before = self.middle_left_right_trace(root)
        self.reverse_tree(root)
        middle_list_after = self.left_middle_right_trace(root)
        first_list_after = self.middle_left_right_trace(root)
        return (middle_list_before == middle_list_after) and (first_list_before == first_list_after)

    def left_middle_right_trace(self, root):
        if root is None:
            return []
        else:
            return self.left_middle_right_trace(root.left) + [root.val] + self.left_middle_right_trace(root.right)

    def middle_left_right_trace(self, root):
        if root is None:
            return []
        else:
            return [root.val] + self.middle_left_right_trace(root.left) + self.middle_left_right_trace(root.right)

    def reverse_tree(self, root):
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return root
        else:
            temp_node = root.left
            root.left = root.right
            root.right = temp_node
            self.reverse_tree(root.right)
            self.reverse_tree(root.left)


if __name__ == '__main__':
    solution = Solution()
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.left.left = TreeNode(3)
    head.right = TreeNode(3)
    head.right.left = TreeNode(2)
    result = solution.isSymmetric(head)
    print(result)
