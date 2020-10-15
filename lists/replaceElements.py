https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            new_arr=arr[i+1:]
            mx=max(new_arr)
            arr[i]=mx
        arr[-1]=-1
        return arr
