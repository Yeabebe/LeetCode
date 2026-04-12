from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        
        # Step 1: XOR all numbers
        for num in nums:
            xor ^= num
        
        # Step 2: Find rightmost set bit
        diff = xor & -xor
        
        a = 0
        b = 0
        
        # Step 3: Split into two groups
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        
        return [a, b]