# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1val = 0
        n=0
        while l1:
            l1val = l1val + l1.val*(10**n)
            n+=1
            l1 = l1.next
            
        l2val = 0
        n=0
        while l2:
            l2val = l2val + l2.val*(10**n)
            n+=1
            l2 = l2.next
            
        val = l1val + l2val
        headNode = pNode =  ListNode()
        while val:
            temp = ListNode(val%10,None)
            val //=10
            pNode.next = temp
            pNode = pNode.next
        
        return headNode.next if headNode.next else ListNode(0,None)

# without coverting to int
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        resHead = pointer = ListNode()
        while l1 and l2:
            pointer.next = ListNode()
            pointer = pointer.next
            sum = l1.val + l2.val + carry
            pointer.val = sum%10
            carry = sum//10
            l1,l2 = l1.next,l2.next
        while l1:
            pointer.next = ListNode()
            pointer = pointer.next
            pointer.val = (l1.val+carry)%10
            carry = (l1.val+carry)//10
            l1 = l1.next
        while l2:
            pointer.next = ListNode()
            pointer = pointer.next
            pointer.val = (l2.val+carry) %10
            carry = (l2.val+carry) //10
            l2 = l2.next
        while carry:
            pointer.next = ListNode()
            pointer = pointer.next
            pointer.val = carry
            carry = 0
        return resHead.next

# cleaner looking, less loops and checks
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resHead = pointer = ListNode()
        carry = 0
        while l1 or l2 or carry:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            sum = l1v+l2v+carry
            carry = sum//10
            pointer.next = ListNode(sum%10)
            pointer = pointer.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return resHead.next