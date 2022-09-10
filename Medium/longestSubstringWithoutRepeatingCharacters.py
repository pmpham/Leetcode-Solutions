# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        dic = {}
        longest = 0
        
        for i,j in enumerate(s):
            if j in dic and left<= dic[j]:
                left = dic[j]+1
                #dic[j]=i
            else:
                longest = max(longest,i-left+1)
            dic[j] = i
        return longest