'''
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        string=''
        while head:
            string+=str(head.val)
            head=head.next
        return(int(string,2))
        
        