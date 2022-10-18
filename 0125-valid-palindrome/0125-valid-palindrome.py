class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Method 1, join string with alpha numeric characters and lowercase
        t = ''.join(filter(str.isalnum, s)).lower()
        # Check if string is equal to reverse
        return t == t[::-1]
    
        