class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        left = 0
        mid = 1
        rigth = 2
        while rigth <= len(arr)-1:        
            # if arr[left] < arr[mid] and arr[mid]< arr[rigth]:
            if arr[left] %2==1 and arr[mid] %2==1 and arr[rigth] %2 == 1:
                    return True
            else:
                left+=1
                mid+=1
                rigth+=1
            # else:
            #     left+=1
            #     mid+=1
            #     rigth+=1
        return False
    
solu = Solution()
print(solu.threeConsecutiveOdds([1,2,3]))
            
                