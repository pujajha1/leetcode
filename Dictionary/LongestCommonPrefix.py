#https://leetcode.com/problems/longest-common-prefix/submissions/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=[]
        k={}
        for i in strs:
            for j in range(0,len(i)):
                l.append(i[:j+1])
        for i in l:
            if(l.count(i)==len(strs)):
                k[i]=len(i)
                
        #checking if dictionary is empty, if not, returns the max from dictionary        
        if not bool(k):
            return ""
        else:
            return max(k, key=k.get)
