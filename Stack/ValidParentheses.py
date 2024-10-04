#https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                curr=stack.pop()
                if curr=='(' :
                    if i!=')':
                        return False
                if curr=='{':
                    if i!='}':
                        return False
                if curr=='[':
                    if i!=']':
                        return False
        if stack:
            return False
        return True


#2nd Way:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesis ={"(":")","{":"}","[":"]"}
        if len(s) % 2 != 0:
            return False

        for i in s :
            if i in paranthesis:
                stack.append(i)
            else:
                if stack ==[] or paranthesis[stack.pop()] != i :
                    return False
        if stack==[]:
            return True 
        else:
            return False

        
