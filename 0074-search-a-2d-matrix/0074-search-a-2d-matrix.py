import bisect
import itertools

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        idx_right = bisect.bisect(list(itertools.chain(*matrix)), target)

        # corner case
        if idx_right == 0:
            return False
        
        exists = list(itertools.chain(*matrix))[idx_right-1] == target
        return exists