from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}
        genes = "ACGT"

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for i in range(8):
                for char in genes:
                    if char == gene[i]:
                        continue

                    new_gene = gene[:i] + char + gene[i + 1:]

                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, mutations + 1))

        return -1