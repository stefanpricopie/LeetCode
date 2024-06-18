from bisect import bisect
from itertools import chain

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flat_matrix = list(chain(*matrix))
        idx_right = bisect(flat_matrix, target)

        # corner case
        if idx_right == 0:
            return False
        
        exists = flat_matrix[idx_right-1] == target
        return exists