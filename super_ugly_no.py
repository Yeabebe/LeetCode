from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        k = len(primes)

        ugly = [1] * n
        idx = [0] * k

        for i in range(1, n):
            nxt = min(primes[j] * ugly[idx[j]] for j in range(k))

            ugly[i] = nxt

            for j in range(k):
                if primes[j] * ugly[idx[j]] == nxt:
                    idx[j] += 1

        return ugly[-1]