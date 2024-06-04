class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        # corner case
        if l == 1:
            return 0

        reach = 0
        max_reach = nums[0]
        jumps = 0
        idx = 0

        while max_reach < l-1:
            idx += 1

            # update jump number and current reach
            if idx > reach:
                jumps += 1
                reach = max_reach

            if idx + nums[idx] > max_reach:
                max_reach = idx + nums[idx]            

        # increment last jump
        return jumps+1
        