class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        for h, citation in enumerate(sorted(citations, reverse=True)):
            if h >= citation:
                return h
        return h+1
        