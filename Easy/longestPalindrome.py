# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/

def longestPalindrome(self, s: str) -> int:
        count = 0
        odd = False
        for i in collections.Counter(s).values():
            if i%2 == 0:
                count+=i
            else:
                odd = True
                count+=i-1
        if odd:
            return count+1
        return count


#somehow faster? below is 3n, top is 2n
def longestPalindrome(self, s: str) -> int:
        ans = 0
        #even = True
        for i in collections.Counter(s).values():
            ans += (i//2) *2
            if ans%2 == 0 and i%2 == 1:
                ans+=1
                #even = False
        return ans