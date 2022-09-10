# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(self, nums: List[int]) -> bool:
        return max(collections.Counter(nums).values())>1