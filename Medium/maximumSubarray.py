# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = 0
        for i in nums:
            curr = max(curr+i,i)
            maxSum = max(curr,maxSum)
        return maxSum
            