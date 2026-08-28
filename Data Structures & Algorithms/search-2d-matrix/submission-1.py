class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # Take first and last values indices
        l, r = 0, rows * cols - 1
        
        while l <= r:
            m = l + (r - l) // 2
            # Find the row and col of m
            row, col = m // cols, m % cols

            # Perform the basic binary search
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False