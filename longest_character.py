class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # Characters that need to be replaced
            window_size = right - left + 1
            replacements = window_size - max_freq

            if replacements > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result