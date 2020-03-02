'''
https://leetcode.com/problems/add-two-numbers/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1=""
        n2=""
        while(l1):
            n1+=str(l1.val)
            l1=l1.next
        
        while(l2):
            n2+=str(l2.val)
            l2=l2.next
        n1=int(n1[::-1])
        n2=int(n2[::-1])
        ans=str(n1+n2)
        ans=(ans[::-1])
        l3=l4=ListNode(0)
        for i in ans:
            l3.next = ListNode(i)
            l3=l3.next
        return l4.next
            