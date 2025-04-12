class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        power_2 = 1
        while 2 * power_2 < n:
            power_2 *= 2
        
        return 1 + self.hammingWeight(n % power_2)