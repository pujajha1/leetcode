#https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted_word=s.strip().split(" ")
        return len(splitted_word[-1])
