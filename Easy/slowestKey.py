# 1629. Slowest Key
# https://leetcode.com/problems/slowest-key/

def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        for i in range(len(releaseTimes)-1):
            releaseTimes[-1-i] -= releaseTimes[-2-i]
        maxTime = max(releaseTimes)
        pos = [i for i, x in enumerate(releaseTimes) if x == maxTime]
        keys = []
        for x in pos:
            keys.append(keysPressed[x])
        return max(keys)
        