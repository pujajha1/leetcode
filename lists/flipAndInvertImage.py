https://leetcode.com/problems/flipping-an-image/submissions/
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        B=[]
        for i in A:
            k=i[::-1]
            B.append(list(map(lambda x:0 if x==1 else 1,k)))
        return B
