"""
Time : O(n)
Space: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        self.helper(root, sum, [], result) 
        return result 
        
        
    def helper(self, node, sum, curr, result):
        if not node:
            return 
        
        curr.append(node.val)
        print(node.val - sum)
        if not node.left and not node.right and node.val == sum:
            result.append(list(curr))
        else:
            self.helper(node.left, sum - node.val, curr, result)
            self.helper(node.right, sum - node.val, curr, result)

        curr.pop()
