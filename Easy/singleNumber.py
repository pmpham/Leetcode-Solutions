# 136. Single Number
# https://leetcode.com/problems/single-number/

def singleNumber(self, nums: List[int]) -> int:
        return min(collections.Counter(nums), key = collections.Counter(nums).get)