#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        n=set(s)
        length=len(s)
        l=list(s)
        k=[]
        t=[]
        s=""
        count=0
        if (len(n)==length):
            return length
        else:
            for i in range(len(l)):
                for j in range(i+1,len(l)+1):
                    if i<j:
                        s=''.join(l[i:j])
                        if (s.count(l[j-1])>=2):
                            break
                        k.append(s)
            for i in range(len(k)):
                t.append(len(k[i]))
            return max(t)
