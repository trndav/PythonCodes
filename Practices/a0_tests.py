class Solution:
    def plusOne(self, digits: int) -> int:
        
        number = int(''.join(map(str, digits)))
        return number
        

x = Solution()
print(x.plusOne([1,2,3]))

digits = [5, 2, 9, 6, 7, 8]
x = range(len(digits)-1,-1,-1)
print(x)