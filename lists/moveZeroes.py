https://leetcode.com/problems/move-zeroes/solution/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z= nums.count(0)
        while z>0:
            if nums.count(0):
                nums.remove(0)
                nums.append(0)
                z=z-1
