class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
          return False
        
        dic = {")":"(","}":"{","]":"["}
        stack = [s[0]]
        tmp = ""
        for i in range(1,len(s)):
          if s[i] in dic:
            if len(stack) == 0 : return False
            tmp = stack.pop()
            if tmp != dic[s[i]]:
              return False
          else:
            stack.append(s[i])
        
        return len(stack) == 0

print(Solution().isValid("()"))        
print(Solution().isValid("(){}}"))        
print(Solution().isValid("([}}])"))