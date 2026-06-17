from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        sorted_nums = sorted(nums)

        mid = (n + 1) // 2

        small = sorted_nums[:mid][::-1]
        large = sorted_nums[mid:][::-1]

        nums[::2] = small
        nums[1::2] = large