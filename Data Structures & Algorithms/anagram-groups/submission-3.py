class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = {}
        for i, stri in enumerate(strs):
            sorted_text = "".join(sorted(stri))
            if sorted_text in matches:
                matches[sorted_text].append(stri)
            else:
                matches[sorted_text] = [stri]
        return list(matches.values())