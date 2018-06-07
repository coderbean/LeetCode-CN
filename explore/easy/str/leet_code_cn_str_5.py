class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = list(s)
        i = 0
        j = len(a) - 1
        while i < j:
            if not a[i].isdigit() and not a[i].isalpha():
                i = i + 1
                continue
            if not a[j].isdigit() and not a[j].isalpha():
                j = j - 1
                continue
            if a[i].upper() != a[j].upper():
                return False
            i = i + 1
            j = j - 1

        return True
