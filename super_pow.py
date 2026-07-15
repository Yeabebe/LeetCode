class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def power(x, n):
            res = 1
            x %= MOD
            while n:
                if n & 1:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                n >>= 1
            return res

        res = 1
        a %= MOD

        for digit in b:
            res = (power(res, 10) * power(a, digit)) % MOD

        return res