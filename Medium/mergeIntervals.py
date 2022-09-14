# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/submissions/

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        low, high = intervals[0][0], intervals[0][1]
        res = []
        for i,interval in enumerate(intervals):
            x = interval[0]
            y = interval[1]
            if low<=x<=y<=high:
                pass
            elif y>high and x<=high:
                high = y
            else:
                res.append([low,high])
                low = x
                high = y
            if i == len(intervals)-1:
                res.append([low,high])
                
        return res

# cleaner code, LC solution   
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for x in intervals:
            if not res or res[-1][1]<x[0]:
                res.append(x)
            else:
                res[-1][1] = max(res[-1][1],x[1])
        return res