class Solution:
    def isPalindrome(self, s: str) -> bool:
        uppercase_text = s.upper()
        l, r = 0, len(s) - 1 

        if len(s) == 1:
            return True
        while l < r: 
            while l < r and not self.isAlpha(uppercase_text[l]):
                l += 1
            print("L = " + uppercase_text[l])
            while r > l and not self.isAlpha(uppercase_text[r]):
                r -= 1
                print("Changed R: " + uppercase_text[r])
            print("R = " + uppercase_text[r])
            
            if uppercase_text[r] != uppercase_text[l]:
                print(uppercase_text[r] + " != " + uppercase_text[l])
                return False        
            print(uppercase_text[r] + " == " + uppercase_text[l])
            l, r = l + 1, r - 1       

        return True

    def isAlpha(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'))