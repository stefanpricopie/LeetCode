class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        step1 = m-1
        step2 = n-1
        for i in range(m+n-1, -1, -1):
            # corner cases
            if step1 == -1:
                # num1 is completed
                nums1[i] = nums2[step2]
                step2 -= 1
                continue
            
            if step2 == -1:
                # num2 is completed
                nums1[i] = nums1[step1]
                step1 -= 1
                continue

            # Compare and replace the largest one
            if nums1[step1] < nums2[step2]:
                nums1[i] = nums2[step2]
                step2 -= 1
            else:
                nums1[i] = nums1[step1]
                step1 -= 1
