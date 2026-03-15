from typing import List,heapq  

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, 0, 0))       
        events.sort()

        res=[[0, 0]]
        heap = [(0, float('inf'))] 

        for x, negH, R in events:
            while heap[0][1] <=x:
                heapq.heappop(heap)

            if negH != 0:
                heapq.heappush(heap, (negH, R))

            curr_height = -heap[0][0]
            if res[-1][1] != curr_height:
                res.append([x, curr_height])   
        return res[1:]

