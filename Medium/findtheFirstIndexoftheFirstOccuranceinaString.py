# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr(self, haystack: str, needle: str) -> int:
        if needle is "":
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1