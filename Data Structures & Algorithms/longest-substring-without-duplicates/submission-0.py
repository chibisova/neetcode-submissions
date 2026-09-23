class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l = 0
        max_len = 0
        for char in range(len(s)):
            while s[char] in visited:
                visited.remove(s[l])
                l+=1
            visited.add(s[char])
            max_len = max(max_len, char - l + 1)

        return max_len

            