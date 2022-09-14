# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/
 
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def isIdentical(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val == t.val:
                return (isIdentical(s.left,t.left) and isIdentical(s.right,t.right))
            return False
        
        stack = [root]
        while stack:
            top = stack.pop()
            #if top.val == subRoot.val:
            if isIdentical(top,subRoot):
                return True
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        return False