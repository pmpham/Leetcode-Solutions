# 704. Binary Search
# https://leetcode.com/problems/binary-search/

def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while True:
            
            mid = ((high+low)//2)
            value = nums[mid]
            
            if value == target:
                return mid
            
            elif (nums[low]>target or nums[high]<target):
                return -1
            
            elif (value>target):
                high = mid-1
    
            else:
                low = mid+1