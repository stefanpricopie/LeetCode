class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        step = 0
        count = 0
        length = len(nums)
        while step < length:
            while step < length and nums[step] == val:
                nums.pop(step)
                count +=1
                length -= 1
            step += 1

        