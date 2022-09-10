# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = None, head
        while fast:
            temp = fast.next
            fast.next = slow
            slow = fast
            fast = temp
        return slow