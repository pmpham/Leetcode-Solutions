# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow = head,head
        while fast:
            try:
                fast = fast.next.next
            except:
                break     
            slow = slow.next
        return slow