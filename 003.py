class Solution:
    def isPalindrome(self, x: int) -> bool:
        inicio = 0
        fin = -1
        while True:
            if x[inicio] == x[fin]:
                inicio = inicio+1
                fin = fin-1
            else:
                return False
        