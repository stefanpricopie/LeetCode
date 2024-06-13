from itertools import permutations

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
            
        def check_constraint(solution):
            """
            :type solution: list
            :rtype: bool
            """
            for i, pos_i in enumerate(solution):
                for j_, pos_j in enumerate(solution[i+1:]):
                    # j = i+1+j_
                    if i-pos_i == i+1+j_ - pos_j:
                        return False
                    if n-1-i-pos_i == n-1-(i+1+j_) - pos_j:
                        return False
            return True
        
        return sum(check_constraint(sol) for sol in permutations(range(n)))