from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = ([False,False,True] + [True] * (n-3)) if n>2 else [False,False]

        sqrtN = int(sqrt(n)) +1

        for i in range(sqrtN):
            if sieve[i]:
                for j in range(i*2,  n, i):
                    sieve[j]=False  

        l = list(filter(lambda x:x , sieve))

        return len(l)
                    