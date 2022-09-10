# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

def myAtoi(self, s: str) -> int:
        nums = "0123456789"
        ops = "-+"
        res = "0"
        mult = 1
        seen = False
        s = s.strip()
        
        for i in s:
            if i in nums:
                res+=i
                seen = True
            elif i in ops:
                if seen:
                    break
                else:
                    seen = True
                    if i == "-":
                        mult *=-1
            else:
                break
        res = int(res)*mult
        if res> 2**31 - 1:
            return 2**31 - 1
        elif res< -2**31:
            return -2**31
        return res