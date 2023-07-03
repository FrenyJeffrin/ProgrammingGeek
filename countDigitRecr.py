class Solution:
    def countDigits(self, n):
        if n <10:
            return 1
        return self.countDigits(n//10)+1
