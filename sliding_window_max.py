class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        res = []
        
        for i in range(len(nums)):
            # Step 1: Remove out-of-window elements
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            # Step 2: Maintain decreasing order
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Step 3: Add current index
            dq.append(i)
            
            # Step 4: Record result
            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return res