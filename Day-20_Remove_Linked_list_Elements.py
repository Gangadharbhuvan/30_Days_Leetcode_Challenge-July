'''
    Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if not head:
            return
        
        prev, cur = None, head
        
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                    cur = cur.next
                else:
                    head = cur.next
                    cur = head
            else:
                prev = cur
                cur = cur.next
        
        return head
