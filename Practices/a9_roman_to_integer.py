'''
Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
'''

class Solution:
    def romanToInt(self, s: str) -> int:

        roman_table = {"I": 1,
                       "V": 5,
                       "X": 10,
                       "L": 50,
                       "C": 100,
                       "D": 500,
                       "M": 1000}
        
        # # Reverse iteration solution
        # num = 0
        # last = "I"
        # for numeral in s[::-1]:
        #     if roman_table[numeral] < roman_table[last]:
        #         print("first loop", roman_table[numeral])
        #         num -= roman_table[numeral]
        #     else:
        #         num += roman_table[numeral]
        #         print("second loop", roman_table[numeral])
        #     last = numeral

        # return num


        # String conversion method
        convert = {"IV": "IIII", "IX": "VIIII",
                   "XL": "XXXX", "XC": "LXXXX",
                   "CD": "CCCC", "CM": "DCCCC"}
        
        for k, v in convert.items():
            s = s.replace(k, v)

        return sum([roman_table[numeral] for numeral in s])

x = Solution()
print(x.romanToInt("MCMXCIV"))


