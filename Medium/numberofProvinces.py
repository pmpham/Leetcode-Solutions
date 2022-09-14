# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/

#personal solution kinda slow
def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        def search(row,col):
            if isConnected[row][col] == 1:
                isConnected[row][col] = 0
                dirs = [(1,0),(-1,0),(0,1),(0,-1)]
                #corns = [(1,1),(-1,1),(-1,-1),(1,-1)]
                for x,y in dirs:
                    for i in range(n):
                        if 0<=row+(x*i)<n and 0<=col+(y*i)<n:
                            search(row+(x*i),col+(y*i))
        res= 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    res+=1
                    search(i,j) 
        return res


# googled solution
def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        
        def search(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in visited:
                    search(j)
                        
        res= 0
        for i in range(n):
            if i not in visited:
                res+=1
                search(i)
        return res