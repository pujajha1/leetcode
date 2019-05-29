#https://leetcode.com/problems/count-primes/submissions/
from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        count=-2
        if (n<=2):
            return 0
        if(n==3):
            return 1
        list_prime=[True]*n
        for i in range(2,int(sqrt(n))+1):
            if list_prime[i]:
                for j in range(i*i,n,i):
                    list_prime[j]=False
        print(list_prime)
        for i in list_prime:
            if i:
                count+=1
        return count
