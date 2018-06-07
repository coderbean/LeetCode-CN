class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list_s = list(s)
        list_t = list(t)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            try:
                list_t.remove(list_s[i])
            except ValueError:
                return False

        return True
