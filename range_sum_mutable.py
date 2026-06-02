from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)

        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, index, delta):
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index

    def _prefixSum(self, index):
        total = 0
        while index > 0:
            total += self.bit[index]
            index -= index & -index
        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefixSum(right + 1) - self._prefixSum(left)