class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        # Check missing character types
        missing = 0

        if not any(c.islower() for c in password):
            missing += 1

        if not any(c.isupper() for c in password):
            missing += 1

        if not any(c.isdigit() for c in password):
            missing += 1

        # Find groups of 3+ consecutive equal characters
        runs = []
        i = 0

        while i < n:
            j = i

            while j < n and password[j] == password[i]:
                j += 1

            length = j - i

            if length >= 3:
                runs.append(length)

            i = j

        # Number of replacements needed to fix repetitions
        replacements = sum(length // 3 for length in runs)

        # Case 1: Too short
        if n < 6:
            return max(missing, 6 - n)

        # Case 2: Length is already within [6, 20]
        if n <= 20:
            return max(missing, replacements)

        # Case 3: Too long
        deletions = n - 20

        # Use deletions to reduce replacements.
        # A deletion is most useful on runs where:
        # length % 3 == 0
        for i in range(len(runs)):
            if deletions == 0:
                break

            if runs[i] % 3 == 0:
                runs[i] -= 1
                deletions -= 1
                replacements -= 1

        # Next, handle runs where length % 3 == 1.
        # Two deletions reduce one replacement.
        for i in range(len(runs)):
            if deletions < 2:
                break

            if runs[i] % 3 == 1:
                use = min(2, deletions)
                runs[i] -= use
                deletions -= use

                if use == 2:
                    replacements -= 1

        # Finally, handle runs where length % 3 == 2.
        # Three deletions reduce one replacement.
        for i in range(len(runs)):
            if deletions < 3:
                break

            if runs[i] % 3 == 2:
                use = min(3, deletions)
                runs[i] -= use
                deletions -= use

                if use == 3:
                    replacements -= 1

        # Every 3 remaining deletions can eliminate one replacement
        replacements -= deletions // 3

        # We must perform all required deletions.
        return (n - 20) + max(missing, replacements)