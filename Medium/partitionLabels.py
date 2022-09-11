# 763. Partition Labels
# https://leetcode.com/problems/partition-labels/

def partitionLabels(self, s: str) -> List[int]:
        left =right = 0
        res = []
        lastIdx = {x:i for i,x in enumerate(s)}
        for i,x in enumerate(s):
            right = max(lastIdx[x],right)
            if i == right:
                res.append(right-left+1)
                left = i+1
        return res