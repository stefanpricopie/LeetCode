class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        heapq.heapify(intervals)

        merged = []
        a = b = None

        while intervals:
            if a is None:
                a, b = heapq.heappop(intervals)
            else:
                c, d = heapq.heappop(intervals)
                if c > b:
                    merged.append([a,b])
                    a, b = c, d
                else:
                    b = max(b,d)
        
        if a is not None:
            merged.append([a,b])
        
        return merged