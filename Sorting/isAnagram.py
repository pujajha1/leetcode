#https://leetcode.com/problems/valid-anagram/submissions/

Bubble Sort:
32/34 cases passed
TimeLimit exceeded

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            s_t=list(s)
            t_t=list(t)
            for i in range(0,len(s_t)):
                for j in range(len(s_t)-(i+1)):
                    if s_t[j]>s_t[j+1]:
                        s_t[j],s_t[j+1]=s_t[j+1],s_t[j]
                    if t_t[j]>t_t[j+1]:
                        t_t[j],t_t[j+1]=t_t[j+1],t_t[j]
            if(s_t==t_t):
                return True
            else:
                return False
