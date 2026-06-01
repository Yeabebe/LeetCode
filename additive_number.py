class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(first, second, start):
            while start < n:
                third = str(first + second)

                if not num.startswith(third, start):
                    return False

                start += len(third)
                first, second = second, first + second

            return True

        for i in range(1, n):
            for j in range(i + 1, n):

                first_str = num[:i]
                second_str = num[i:j]

                # No leading zeros
                if len(first_str) > 1 and first_str[0] == '0':
                    continue

                if len(second_str) > 1 and second_str[0] == '0':
                    continue

                first = int(first_str)
                second = int(second_str)

                if valid(first, second, j):
                    return True

        return False