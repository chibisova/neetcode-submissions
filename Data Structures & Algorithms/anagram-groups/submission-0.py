class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = {}
        output = []

        for i, stri in enumerate(strs):
            sorted_text = "".join(sorted(stri))
            if sorted_text in matches:
                matches[sorted_text].append(stri)
            else:
                matches[sorted_text] = [stri]
        # we have a dict in form: 
        #   {"sorted_str": ["str1", "str2"]}
        # we need to return:
        #   [["str1", "str2"],["str0"]]
        return list(matches.values())