https://leetcode.com/problems/contains-duplicate/submissions/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0 or len(nums)==1:
            return False
        l=list(set(nums))
        l.sort()
        nums.sort()
        if l==nums:
            return False
        else:
            return Tru
