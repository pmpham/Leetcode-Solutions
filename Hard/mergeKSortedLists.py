# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/submissions/

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while None in lists:
            lists.remove(None)
        if not lists:
            return None
        
        resHead = tempHead = ListNode()
        
        while len(lists)>1:
            remember = (float('inf'),0)
            for i,node in enumerate(lists):
                if node.val<remember[0]:
                    remember = (node.val,i)
            tempHead.val = remember[0]
            tempHead.next = ListNode()
            tempHead = tempHead.next
            if lists[remember[1]].next:
                lists[remember[1]] = lists[remember[1]].next
            else:
                del lists[remember[1]]
        tempHead.val = lists[0].val
        tempHead.next = lists[0].next
        return resHead

# way more efficient implimentation
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for ll in lists:
            while ll:
                values.append(ll.val)
                ll = ll.next
        head = temp = ListNode()
        for x in sorted(values):
            temp.next = ListNode(x)
            temp = temp.next
        return head.next