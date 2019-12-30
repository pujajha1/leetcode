#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter=0
        for i in nums:
            if(len(str(i)) % 2==0):
                counter=counter+1
            continue
        return counter
