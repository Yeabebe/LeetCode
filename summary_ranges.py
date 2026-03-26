class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        
        if n == 0:
            return res
        
        start = nums[0]
        
        for i in range(1, n + 1):
            # if end of array OR break in consecutive sequence
            if i == n or nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{end}")
                
                if i < n:
                    start = nums[i]
        
        return res