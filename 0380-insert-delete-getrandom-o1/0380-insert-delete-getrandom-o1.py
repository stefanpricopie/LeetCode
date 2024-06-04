import random

class RandomizedSet(object):

    def __init__(self):
        # I assume that the set has unique items. I don't find the example very clear
        self.randset = []        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.randset:
            return False
        else:
            self.randset.append(val)
            return True     

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.randset:
            self.randset.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.randset)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()