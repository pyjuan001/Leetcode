class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        index = -1
        x=str(x)
        for i in range(0, len(x)):
            if x[i] == x[index]:
                index-=1
            else:
                return False
        return True


sol = Solution()
print(sol.isPalindrome(101))