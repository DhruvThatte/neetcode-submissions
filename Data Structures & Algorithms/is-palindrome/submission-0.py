class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Filter out non-alphanumeric and convert to lowercase
        filtered = [c.lower() for c in s if c.isalnum()]
    # Compare with the reversed list
        return filtered == filtered[::-1]