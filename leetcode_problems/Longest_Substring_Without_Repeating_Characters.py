class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       x=set()
       maximum=0
       start=0
       end=0
       while end<len(s):
           if s[end] not in x:
               x.add(s[end])
               end+=1
               maximum=max(maximum,len(x))
           else:
                x.remove(s[start])
                start+=1
       return maximum

x=Solution()
print(x.lengthOfLongestSubstring("abcabcbb"))
print(x.lengthOfLongestSubstring('bbbb'))
print(x.lengthOfLongestSubstring("pwwkew"))