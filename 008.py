class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        lista=[None] *n
        rigth = len(s)
        rigth-=1
        left = 0
        print(lista)
        while left<=rigth:
            if s[left] == s[rigth]: 
                lista[left] = s[left] 
                lista[rigth] = s[left]
                print(lista)
                left +=1
                rigth-=1

            else:
                if s[left]< s[rigth]:
                    lista[left] = s[left]
                    lista[rigth] = s[left]
                    left+=1
                    rigth-=1
                    print(lista)
                    
                    # lista.append(i)
                else:
                    # s[left] = rigth
                    lista[left]  = s[rigth]
                    lista[rigth] = s[rigth]
                    left+=1
                    rigth-=1
                    print(lista)
                    # lista.append(i)
        return "".join(lista)
       
                
        


s = "abcd"
solu = Solution()
print(solu.makeSmallestPalindrome(s))


