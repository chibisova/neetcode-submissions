class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += string + "ы"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = ['']
        i = 0
        if s:
            for c, char in enumerate(s):
                if char != "ы":
                    decoded_strs[i] += char
                elif c != (len(s)-1):
                    decoded_strs.append('')
                    i += 1
        else:
            decoded_strs=[]
        return decoded_strs