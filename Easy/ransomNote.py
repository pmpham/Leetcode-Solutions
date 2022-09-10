# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''for i in ransomNote:
            if ransomNote.count(i)> magazine.count(i):
                return False
        return True'''
        ransomLetters = [*set(sorted(ransomNote))]
        for i in ransomLetters:
            if ransomNote.count(i)> magazine.count(i):
                return False
        return True