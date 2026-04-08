class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        @lru_cache(None)
        def dfs(expr):
            res = []
            
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = dfs(expr[:i])
                    right = dfs(expr[i+1:])
                    
                    for l in left:
                        for r in right:
                            if ch == '+':
                                res.append(l + r)
                            elif ch == '-':
                                res.append(l - r)
                            else:
                                res.append(l * r)
            
            # Base case: number
            if not res:
                res.append(int(expr))
            
            return res
        
        return dfs(expression)