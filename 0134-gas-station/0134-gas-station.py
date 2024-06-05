class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # corner case
        if sum(cost) > sum(gas):
            return -1
        
        l = len(gas)

        total = 0

        start = 0
        end = 0
        stations = 0
        increment = True

        while start < l:
            if increment:
                total += gas[end] - cost[end]
                # increment stations
                stations += 1

            if total >= 0:
                # check if circuit complete
                if stations == l:
                    return start

                # increment end, ensure index range
                end = (end+1)%l
                increment = True
            else:
                # move start to the right
                total -= gas[start] - cost[start]
                stations -= 1

                if stations == 0:
                    # increment both start and end (no need for %l)
                    start += 1
                    end += 1
                    # add end
                    increment = True
                else:
                    # increment start only (start is before end)
                    start += 1
                    
                    # end was already added
                    increment = False

        return -1