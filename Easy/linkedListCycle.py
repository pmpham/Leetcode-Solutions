# 141. LinkedListCycle
# https://leetcode.com/problems/linked-list-cycle/

def hasCycle(self, head):
        #map = {head:0}
        slowhead = head
        fasthead = head
        #counter = 0
        while True:
            try:
                fasthead = fasthead.next.next
            except:
                return False
            slowhead = slowhead.next
            #counter+=1
            if slowhead == fasthead:
                return (True)