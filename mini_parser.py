from typing import NestedInteger

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # Single integer
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = 0
        sign = 1
        in_num = False

        for ch in s:
            if ch == '[':
                stack.append(NestedInteger())

            elif ch == '-':
                sign = -1

            elif ch.isdigit():
                num = num * 10 + int(ch)
                in_num = True

            elif ch == ',' or ch == ']':
                if in_num:
                    stack[-1].add(NestedInteger(sign * num))
                    num = 0
                    sign = 1
                    in_num = False

                if ch == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)

        return stack[-1]