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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        d = {}
        self.pre(root,d,1)
        lst = []
        
        
        for i in range(1,len(d)+1):
            if i % 2 == 1:
                lst.append(d[i])
            else:
                l = list(d[i])
                lst.append(l[::-1])
            
        return lst
        
    
    def pre(self,t,d,l):
        if not t:
            return
        
        d.setdefault(l,[]).append(t.val)
        self.pre(t.left,d,l+1)
        self.pre(t.right,d,l+1)