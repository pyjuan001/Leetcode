list_output = []
nums = [0,1,1]

class Solution(object):
 def prefixesDivBy5(self, nums):
  valor = 0
  for i in nums:
     nuevo_numero = valor *2 +i
     if nuevo_numero % 5 == 0:
        list_output.append(True)
     else:
        list_output.append(False)
     valor = nuevo_numero
  return list_output
 
s = Solution()
print(s.prefixesDivBy5(nums))
