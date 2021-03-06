'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

#层次遍历的一个变种，增加一个标志来判断是否变向


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level, res = [root], []
        order = 0 # define which direction to output vals, 0 means l->r, 1 means r->l
        while level and root:
            if order == 0:
                res.append([node.val for node in level])
            if order == 1:
                res.append([node.val for node in level][::-1])
            LRpair = [(node.left, node.right) for node in level]
            level = [node for pair in LRpair for node in pair if node]
            order = 1-order
        return res
