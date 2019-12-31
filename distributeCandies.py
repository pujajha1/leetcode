#https://leetcode.com/problems/distribute-candies/submissions/
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        set_length=len(list(set(candies)))
        half_length=len(candies)//2
        if(set_length<=half_length):
            return set_length
        elif(set_length>half_length):
            return half_length
