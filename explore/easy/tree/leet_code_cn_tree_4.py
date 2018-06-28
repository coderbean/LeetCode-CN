from queue import Queue


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LevelNode(object):
    def __init__(self, x, y):
        self.node = x
        self.level = y


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = list()
        temp_queue = Queue()
        temp_queue.put(LevelNode(root, 0))
        while not temp_queue.empty():
            node = temp_queue.get()
            if node.level + 1 > len(ans):
                ans = ans + [list()]
            ans[node.level].append(node.node.val)
            if node.node.left:
                temp_queue.put(LevelNode(node.node.left, node.level + 1))
            if node.node.right:
                temp_queue.put(LevelNode(node.node.right, node.level + 1))
        return ans


if __name__ == '__main__':
    solution = Solution()
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.left.left = TreeNode(3)
    head.right = TreeNode(3)
    head.right.left = TreeNode(2)
    result = solution.levelOrder(head)
    print(result)
