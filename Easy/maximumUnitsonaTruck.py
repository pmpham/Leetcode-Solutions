# 1710. Maximum Units on a Truck
# https://leetcode.com/problems/maximum-units-on-a-truck/

def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:-x[1])
        count = 0
        for box,unit in boxTypes:
            if truckSize >= box:
                truckSize-=box
                count += box*unit
            else:
                count+=truckSize*unit
                break
        return count