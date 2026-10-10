class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # frequency map
        res = 0

        l = 0
        maxfreq = 0 # character frequency
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # return 0 if its a new character
            maxfreq = max(maxfreq, count[s[r]])

            while (r - l + 1) - maxfreq > k: # if the number of replacements is greater than allowed
                count[s[l]] -= 1  # remove the left character from the window
                l += 1 # shift the left pointer
            res = max(res, r - l + 1)

        return res