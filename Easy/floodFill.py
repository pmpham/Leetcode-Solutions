# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        firstColor = image[sr][sc]
        if firstColor == color:
            return image
        r,c = len(image),len(image[0])
        
        def search(row,col):
            if image[row][col] == firstColor:
                image[row][col] = color
                dirs = [(-1,0),(1,0),(0,-1),(0,1)]
                for x,y in dirs:
                    if 0<=row+x<r and 0<=col+y<c:
                        search(row+x,col+y)
        search(sr,sc)
        return image