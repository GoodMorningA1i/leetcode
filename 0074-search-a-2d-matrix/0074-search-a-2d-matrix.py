class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1,3,5,7,10,11,16,20,23,30,34,60
        """

        #binary search on rows
        t, b = 0, len(matrix) - 1

        while t <= b:
            midRow = (t + b)// 2

            if target < matrix[midRow][0]:
                b = midRow - 1
            elif matrix[midRow][-1] < target:
                t = midRow + 1
            else:
                #binary search on columns
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    midCol = (l + r) // 2
                    print(matrix[midRow][midCol])
                    if target < matrix[midRow][midCol]:
                        r = midCol - 1
                    elif target > matrix[midRow][midCol]:
                        l = midCol + 1
                    else:
                        return True   
                
                return False

        return False