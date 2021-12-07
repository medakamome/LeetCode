from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    mlen = max([len(x) for x in strs])
    ret = ""
    for n in range(1,mlen+1):
      if len(list(set([s[:n] for s in strs]))) == 1:
        ret = strs[0][:n]
      else:
        break

    return ret

print(Solution().longestCommonPrefix(["aiueo","aa","aaaiueo"]))
print(Solution().longestCommonPrefix(["aaiueo","aaiu","aaiueo"]))