class Solution:
    def integerReplacement(self, n: int) -> int:
        operations = 0

        while n != 1:
            if n % 2 == 0:
                # Even: divide by 2
                n //= 2

            elif n == 3:
                # Special case
                n -= 1

            elif n % 4 == 1:
                # ...01 in binary
                # n - 1 gives a number divisible by 4
                n -= 1

            else:
                # ...11 in binary
                # n + 1 gives a number divisible by 4
                n += 1

            operations += 1

        return operations