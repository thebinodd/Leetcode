'''

242. Valid Anagram

Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

'''


# -----Brute Force Approach-----

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if(len(s) == 1):
#             return True

#         if(len(s)!=len(t)):
#             return False

#         for i in range(0, len(t)):

#             if(t[i] not in s):
#                 return False
                

#         return True




#----- Optimal Approach-----

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False

        return True



#-----Test Case-----

test = Solution()
print(test.isAnagram("anagram" , "nagaram"))


        