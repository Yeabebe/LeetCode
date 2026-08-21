class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        number = 0

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == '[':
                # Save the current string and repeat count
                stack.append((current, number))

                current = ""
                number = 0

            elif ch == ']':
                # Get the previous string and repeat count
                prev_string, repeat = stack.pop()

                current = prev_string + current * repeat

            else:
                # Normal character
                current += ch

        return current