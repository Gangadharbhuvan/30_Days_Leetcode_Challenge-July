'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (0,-1), (0, 1), (1,0)]
        height, width = len(board), len(board[0])
        
        def helper(r, c, ind): # ind for index, aka which letter we are focusing on now
            if ind == len(word): ## if checked through all letters of the word, return True 
                return True
            for group in directions:
                newr, newc = r+group[0], c+ group[1] 
                if newr >= 0 and newr < height and newc >= 0 and newc < width:  # checking boundaries 
                    if board[newr][newc] == word[ind]:
                        board[newr][newc] = '' # set to None to prevent double traversal 
                        if helper(newr, newc, ind+1):
                            return True 
                        board[newr][newc] = word[ind] # set back to original so that it could be used again
            
        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    board[i][j] = '' ## set this to none, so that it wouldn't be travsersed twice! 
                    if helper(i, j, 1):
                        return True 
                    board[i][j] = word[0] # set back to original so that it could be used again 
        return False 
		