class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        j = 1  # Pointer for the position to place the next unique element
        for i in range(2, len(nums)):
            if nums[j] != nums[i] or (nums[j] == nums[i] and nums[j-1] != nums[i]):
                j += 1
                nums[j] = nums[i]
        
        return j + 1