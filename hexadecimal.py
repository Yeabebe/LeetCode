class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = []

        # Process exactly 32 bits
        for _ in range(8):
            digit = num & 0xF
            result.append(hex_chars[digit])
            num >>= 4

            # Stop once all useful bits are processed
            if num == 0:
                break

        return ''.join(result[::-1])