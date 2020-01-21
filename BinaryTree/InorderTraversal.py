class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        
        leftlist = self.inorderTraversal(root.left)
        
        rootlist = [root.val]
        
        rightlist = self.inorderTraversal(root.right)
        
        ans = leftlist + rootlist + rightlist
        
        return ans
