class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        l = len(ratings)
        candies = l

        # min \i/ if smaller than both neighbours then 1 candy

        # eq -i- or \i- or -i/ then 1 candy

        # dominated \i\ or /i/ candy is distance to its respective min or eq +1

        # dominating /i\ candy is max of the distance between itself and
        # the min or eq on either side (left or right) +1
        
        last_1candy_idx = 0
        last_maxcandy_idx = 0
        last_max_candies = 1

        prev_rating = ratings[0]

        for i, rating in enumerate(ratings[1:]):
            if prev_rating < rating:
                # update last_1candy_idx and
                # reset last candies only if decreasing previously 
                if last_1candy_idx == i:
                    # \i/ so i is a new last 1 candy
                    last_maxcandy_idx = i
                    last_max_candies = 1

                # maxcandy_idx and its candy are higher by 1
                last_maxcandy_idx += 1
                last_max_candies += 1

                # last maxcandy_idx should be current step
                assert last_maxcandy_idx == i+1
                
                # candies at i+1 are 1 + (i+1) - last_1candy_idx
                candies += last_maxcandy_idx - last_1candy_idx
            
            elif prev_rating > rating:
                # update last_1candy_idx only if increasing previously 
                if last_maxcandy_idx == i:
                    # /i\ so i is a new last max candy
                    last_1candy_idx = i

                # update last_1candy_idx to current step
                last_1candy_idx += 1

                # last last_1candy_idx should be current step
                assert last_1candy_idx == i+1

                # last_max_candies needs increasing if ...
                if last_1candy_idx - last_maxcandy_idx == last_max_candies:
                    last_max_candies += 1
                    candies += last_1candy_idx - last_maxcandy_idx
                else:
                    # increment up until last_maxcandy_idx + 1
                    candies += last_1candy_idx - last_maxcandy_idx - 1
            else:
                # no higher ranking condition to satisfy
                last_1candy_idx = last_maxcandy_idx = i+1
                last_max_candies = 1

            prev_rating = rating

        return candies
