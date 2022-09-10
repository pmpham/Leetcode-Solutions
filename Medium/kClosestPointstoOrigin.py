# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(points)<=k:
            return points
        dick = {}
        lengths = []
        for pair in points:
            length = math.sqrt((pair[0]**2) + (pair[1]**2))
            lengths.append(length)
            if length in dick:
                dick[length].append(pair)
            else:
                dick[length] = [pair]
        lengths.sort()
        res = []
        for i in range(0,k):
            res.append(dick[lengths[i]][0])
            dick[lengths[i]].remove(dick[lengths[i]][0])
            
        return res