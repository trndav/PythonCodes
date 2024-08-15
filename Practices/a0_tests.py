class Solution:
    def plusOne(self, digits: int) -> int:
        
        number = int(''.join(map(str, digits)))
        return number
        

x = Solution()
print(x.plusOne([1,2,3]))