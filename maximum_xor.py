from typing import List     

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        answer = 0
        mask = 0

        # nums[i] <= 2^31 - 1, so check 31 bits
        for bit in range(30, -1, -1):
            mask |= (1 << bit)

            prefixes = set()

            for num in nums:
                prefixes.add(num & mask)

            # Try setting the current bit to 1
            candidate = answer | (1 << bit)

            found = False

            for prefix in prefixes:
                if (prefix ^ candidate) in prefixes:
                    found = True
                    break

            if found:
                answer = candidate

        return answer