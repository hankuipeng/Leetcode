# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.solution_list = []
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return self.solution_list
        else:
            # Insert current node vlaue
            self.solution_list.append(root.val)

            # Traverse left first
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

        return self.solution_list    
