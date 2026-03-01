class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # Build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # Queue for courses with no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        finished = 0
        
        while queue:
            course = queue.popleft()
            finished += 1
            
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return finished == numCourses