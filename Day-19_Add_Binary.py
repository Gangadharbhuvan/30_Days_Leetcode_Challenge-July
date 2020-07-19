'''
	Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

'''

class Solution:
    def addBinary(self, a, b):
        i, j, summ, carry = len(a) - 1, len(b) - 1, "", 0
        while i >= 0 or j >= 0 or carry:
            d1 = int(a[i]) if i >= 0 else 0
            d2 = int(b[j]) if j >= 0 else 0
            summ += str((d1 + d2 + carry) % 2)
            carry = (d1 + d2 + carry) // 2
            i, j = i-1, j-1 
        return summ[::-1]