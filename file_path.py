class Solution:
    def lengthLongestPath(self, input: str) -> int:
        longest = 0

        # length[d] = total path length up to depth d
        length = {0: 0}

        for line in input.split("\n"):
            depth = line.count("\t")
            name = line.lstrip("\t")

            if "." in name:
                # File
                longest = max(longest, length[depth] + len(name))
            else:
                # Directory (+1 for '/')
                length[depth + 1] = length[depth] + len(name) + 1

        return longest