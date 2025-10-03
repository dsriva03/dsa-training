def longest_substring(s: str) -> int:

    seen = set()

    left = 0

    max_length = 0

    for r in range(len(s)):

        while (s[r] in seen):
            seen.remove(s[left])
            left += 1
        
        seen.add(s[r])

        max_length = max(max_length, r - left + 1)


    
    return max_length


def longest_substring_map(s: str) -> int:

    seen = {}

    max_length = 0

    left = 0

    for r in range(len(s)):

        if s[r] in seen:
            left = max(left, seen[s[r]] + 1)

        seen[s[r]] = r
        max_length = max(max_length, r - left + 1)
    
    return max_length



def longest_substring_string(s: str) -> str:
    max_length = 0
    max_start = 0
    left = 0

    seen = set()

    for r in range(len(s)):

        while s[r] in seen:
            seen.remove(left)
            left += 1

        seen.add(s[r])

        if r - left + 1 > max_length:
            max_length = r - left + 1
            max_start = left
    
    return s[max_start: max_start + max_length]




