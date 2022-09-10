# 1603. Design Parking System
# https://leetcode.com/problems/design-parking-system/

def __init__(self, big: int, medium: int, small: int):
        self.spaces = {1:big,2:medium,3:small}

def addCar(self, carType: int) -> bool:
    self.spaces[carType] -= 1
    
    return self.spaces[carType] + 1 > 0