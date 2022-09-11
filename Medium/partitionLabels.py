# 763. Partition Labels
# https://leetcode.com/problems/partition-labels/

def partitionLabels(self, s: str) -> List[int]:
        left = 0
        right = 0
        res = []
        for i,x in enumerate(s):
            if i<=right:
                if len(s)-1-s[::-1].index(x)>right:
                    right = len(s)-1-s[::-1].index(x)
            
            else:
                res.append(right-left+1)
                right = len(s)-1-s[::-1].index(x)
                left = i
        res.append(right-left+1)
        return res