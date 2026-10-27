class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[]
        for i in range(m):
            row=[]
            for j in range(n):
                if i ==0 and j<n-1:
                    row.append(".")
                elif j==n-1:
                    row.append(".")
                else:
                    row.append("#")
            grid.append(''.join(row))
        return grid
    
        