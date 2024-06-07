class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # level of water at i is min(cummax(x[:i]), cummax(x[-1:-i-1:-1]))
        
        l = len(height)

        next_peak = [0] * l
        peak = 0

        # get cummax(x[-1:-i-1:-1])
        for i in range(-1,-1-l,-1):
            peak = max(peak, height[i])
            next_peak[i] = peak
        
        # reset peak
        peak = 0

        # set total water
        total_water = 0

        # water contained is (min(p, next_p) - h)+
        # where ()+ means its non-negative
        for (h, next_p) in zip(height, next_peak):
            peak = max(peak, h)
            water = min(peak, next_p) - h
            if water > 0:
                total_water += water
        
        return total_water
        