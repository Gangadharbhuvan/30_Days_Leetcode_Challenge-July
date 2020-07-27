'''
    Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7



'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def formTree(self, postorder, inorder, start, end):
        if start > end:
            return None
        
        root = TreeNode(postorder[self.postIndex])
        self.postIndex -= 1 #decrement

        if root is None:
            return None
          
        if start == end:
            return root
        
        index = self.inorder_hashmap[root.val]

        #traversal
        root.right = self.formTree(postorder, inorder, index+1, end)
        root.left = self.formTree(postorder, inorder, start, index - 1)
        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        #preorder -> Root, Left, Right
        #inorder -> Left, root, Right
        #postorder -> Left, Right, Root

        self.inorder_hashmap = {}
        self.postIndex = len(postorder) - 1

        for num, i in enumerate(inorder):
            self.inorder_hashmap[i] = num
        
        return self.formTree(postorder, inorder, 0, len(inorder)-1)