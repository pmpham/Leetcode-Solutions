# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            return collections.Counter(s) == collections.Counter(t)
        return False