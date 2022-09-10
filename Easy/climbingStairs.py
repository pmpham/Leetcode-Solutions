# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1 or n==2:
            return n
        pp = 1
        p = 2
        curr = 0
        for i in range(3,n+1):
            curr = pp +p
            pp = p
            p = curr
        return curr