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
                