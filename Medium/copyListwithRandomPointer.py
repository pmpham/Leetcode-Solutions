# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        temp = head
        
        while temp:
            copy = Node(x=temp.val,next = temp.next, random = temp.random)
            temp.next = copy
            temp = temp.next.next
        
        newHead = head.next
        
        while newHead:
            if newHead.next:
                newHead.next = newHead.next.next
            if newHead.random:
                newHead.random = newHead.random.next
            else:
                newHead.random = None
            newHead = newHead.next
        return head.next