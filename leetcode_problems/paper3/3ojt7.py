# 7.Write a function that accepts two strings and returns True if the two strings are anagrams 
# of each other.

def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return True
    return False



print(anagram('listen','silent'))
print(anagram('dad','bad'))
