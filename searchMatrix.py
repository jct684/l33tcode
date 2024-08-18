class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def rowSearch(matrix, target):
            outer_left = 0
            outer_right = len(matrix) - 1
            while outer_left < outer_right:
                outer_mid = (outer_left + outer_right) // 2
                if (matrix[outer_mid][0] <= target and matrix[outer_mid][-1] >= target) or matrix[outer_mid][0] > target:
                    outer_right = outer_mid
                else:
                    outer_left = outer_mid + 1
            if matrix[outer_left][0] <= target and matrix[outer_left][-1] >= target:
                return outer_left
            else:
                return -1
        
        def columnSearch(row, target):
            left = 0
            right = len(row) - 1
            while left < right:
                mid = (left + right) // 2
                if row[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            if row[left] == target:
                return True
            else:
                return False
        
        row_index = rowSearch(matrix, target)
        if row_index == -1:
            return False
        return columnSearch(matrix[row_index], target)