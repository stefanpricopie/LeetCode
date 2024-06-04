class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        # corner case if k >= l
        k %= l

        # count swaps
        count = l

        # start index
        start = -1

        while count > 0:
            start += 1
            i = start
            queue = nums[i]

            while True:
                j = (i + k) % l
    
                save = nums[j]
                nums[j] = queue
                queue = save

                i = j
                count -= 1

                if i == start:
                    break
