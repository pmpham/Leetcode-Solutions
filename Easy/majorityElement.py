# 169. Majority Element
# https://leetcode.com/problems/majority-element/

def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key = counts.get)