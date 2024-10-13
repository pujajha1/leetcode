class Solution:
    def fib(self, n: int) -> int:
        fib_list=[0,1,1]
        if n in [0,1,2]:
            return fib_list[n]
        else:
            return int(self.fib(n-1) + self.fib(n-2))
        
