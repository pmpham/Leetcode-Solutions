# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        mergelistp = ListNode()
        listhead = mergelistp
        
        while (p1.next != None) or (p2.next !=None):
            if p1.val < p2.val:
                mergelistp.val = p1.val
                mergelistp.next = ListNode(val = None,next = None)
                mergelistp = mergelistp.next
                p1 = p1.next
            else:
                mergelistp.val = p2.val
                mergelistp.next = ListNode(val = None,next = None)
                mergelistp = mergelistp.next
                p2 = p2.next
        
        if p1 != None:
            mergelistp = p1
        elif p2 != None:
            mergelistp = p2
    
        return listhead