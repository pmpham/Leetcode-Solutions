# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        #seen = []
        res = 0
        
        def search(row:int, col:int):
            if grid[row][col] =="0":
                return
            grid[row][col] = "0"
            dirs = [(-1,0), (1,0), (0,-1), (0,1)]
            for x,y in dirs:
                if 0<= row+ x<rows and 0<=col+y<cols:
                    search(row+x, col+y)
                '''try:
                    search(row+1, col)
                except:
                    pass
                try:
                    search(row-1, col)
                except:
                    pass
                try:
                    search(row, col+1)
                except:
                    pass
                try:
                    search(row, col-1)
                except:
                    pass
            else:
                pass'''
                    
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    search(i,j)
                    res+=1
                    
        return res