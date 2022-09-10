# 2130. Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        values= []
        n = 0 
        while head:
            values.append(head.val)
            head = head.next
        sums = []
        for i in range(len(values)//2):
        
            sums.append(values[i]+values[-1-i]) 
        return max(sums)
        