class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        hash = {}
        for i in bulbs:
            if i not in hash:
                hash[i] = 0
            elif i in hash and hash[i] == 0:
                hash[i] = 1
            elif i in hash and hash[i] == 1:
                hash[i] = 0
            
            print(hash)
        return(sorted([key for key in hash if hash[key] == 0]))




sol = Solution()
print(sol.toggleLightBulbs([10,30,20,10]))