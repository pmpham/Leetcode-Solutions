# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

def maxArea(self, height: List[int]) -> int:
        most = 0
        l = 0
        r = len(height)-1
        while l<r:
            most = max(most,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return most