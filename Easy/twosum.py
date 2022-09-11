# 1. Two Sum
# https://leetcode.com/problems/two-sum/

def twoSum(self, nums: list[int], target: int) -> list[int]:
        values= {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in values:
                return ([i,values[compliment]])
            else:
                values[nums[i]] = i

#faster
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i=0
        seen={}
        for i,x in enumerate(nums):
            if target-x in seen:
                return [i,seen[target-x]]
            else:
                seen[x] = i
                