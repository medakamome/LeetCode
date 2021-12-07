class Solution:
  def romanToInt(self, s:str) -> int:
    roman = {
      "I":1,
      "V":5,
      "X":10,
      "L":50,
      "C":100,
      "D":500,
      "M":1000
    }

    total = 0
    n = len(s) -1
    prec = 0
    while n >= 0:
      r = roman[s[n]]
      total += -r if r < prec else r
      prec = r
      n -= 1
    
    return total


print(Solution().romanToInt("III"))
print(Solution().romanToInt("IV"))
print(Solution().romanToInt("IX"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))