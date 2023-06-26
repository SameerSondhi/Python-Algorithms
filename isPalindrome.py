# Given an integer, determine if the integer is a palindrome or not
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]