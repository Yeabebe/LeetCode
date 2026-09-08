class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequencies = {}

        for char in s:
            frequencies[char] = frequencies.get(char, 0) + 1

        length = 0
        has_odd = False

        for count in frequencies.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                has_odd = True

        if has_odd:
            length += 1

        return length