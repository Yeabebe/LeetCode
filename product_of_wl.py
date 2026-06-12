class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)

        masks = [0] * n
        lengths = [0] * n

        for i, word in enumerate(words):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))

            masks[i] = mask
            lengths[i] = len(word)

        max_product = 0

        # Compare every pair of words
        for i in range(n):
            for j in range(i + 1, n):
                # No common letters
                if masks[i] & masks[j] == 0:
                    max_product = max(
                        max_product,
                        lengths[i] * lengths[j]
                    )

        return max_product