# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number

#iterative bottom up
def fib(self, n):
        if n<2:
            return n
        
        pp = 0
        p = 1
        curr = 0
        for i in range(2,n+1):
            curr = pp +p
            pp = p
            p = curr
        return curr

#recursive
dic = {0:0,1:1}
def fib(self, n: int) -> int:
    
    if n in self.dic:
        return self.dic[n]
    else:
        self.dic[n] = self.fib(n-1)+self.fib(n-2)
        return self.dic[n]