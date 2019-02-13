
#https://leetcode.com/problems/two-sum/submissions/

class Solution(object):
    def twoSum(self, nums, target):
        B=[]
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            j=target-nums[i]
            #print(i,j)
            if (j in nums and i!=nums.index(j)):
                B.append(i)
                B.append(nums.index(j))
                break
            continue
        return B
                 
