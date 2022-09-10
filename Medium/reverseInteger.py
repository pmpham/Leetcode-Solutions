# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/

def reverse(self, x: int) -> int:
        #x = str(x)[::-1]
        low = -2**31
        high = 2**31-1
        ans = 0 
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)
            
            if ans > high//10 or (ans == high//10 and digit>=high%10):
                return 0
            elif ans <low //10 or (ans == low//10 and digit<=low%10):
                return 0
            ans = ans*10 + digit
            
        return ans
            