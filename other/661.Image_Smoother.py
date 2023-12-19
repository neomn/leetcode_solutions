class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])
        res = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                sum, count = 0, 0
                if i-1 in range(row) and j-1 in range(col): 
                    sum += img[i-1][j-1]
                    count += 1
                if i-1 in range(row) and j in range(col): 
                    sum += img[i-1][j]
                    count += 1
                if i-1 in range(row) and j+1 in range(col):
                    sum += img[i-1][j+1]
                    count += 1
                if i in range(row) and j-1 in range(col):
                    sum += img[i][j-1]
                    count += 1
                if i in range(row) and j in range(col):
                    sum += img[i][j]
                    count += 1
                if i in range(row) and j+1 in range(col):
                    sum += img[i][j+1]
                    count += 1
                if i+1 in range(row) and j-1 in range(col):
                    sum += img[i+1][j-1]
                    count += 1
                if i+1 in range(row) and j in range(col):
                    sum += img[i+1][j]
                    count += 1
                if i+1 in range(row) and j+1 in range(col):
                    sum += img[i+1][j+1]
                    count += 1

                res[i][j] = sum//count
        return res
        
