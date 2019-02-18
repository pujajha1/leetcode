class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        l=[]
        if target==0:
            return 0
        if target>nums[-1]:
            return len(nums)
        for i in nums:
            if(target<=i):
                l.append((nums.index(i)))
        return (min(l))
