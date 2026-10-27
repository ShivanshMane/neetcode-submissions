'''
Understanding the problem = 
    Input = string s 
    Goal = find out the lonest substring s that is a palindrome
    Ouput = return the longest palindrome which is substring of s 
Constraints = what if string has just one letter
            = what is the max length of s
            = can s contain digits 
            = is it all uppercase or lowercase
Examples = Input: s = "ababd", Output: "bab"
         = Input: s = "abbc", Output: "bb"
         = Input: s = "a", Output: "a"
Approach - > The brute force approach 
         = create all possible substrings
         = check any palindrome 
         = keep longest 
         = o(n^3)
         -> Optimal Approach 
         = if a palindrome, the characters match from centre whether left or right 
         = Chose centre and expand symetrically until characters match 
         = Time Complexity - o(n^2) and Space Complexity - o(1)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0 
        resLen = 0 
        for i in range(len(s)):
            # odd length 
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l 
                    resLen = r - l + 1
                l -= 1
                r += 1 
            #even length 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l 
                    resLen = r - l + 1
                l -= 1 
                r += 1
        return s[resIdx : resIdx + resLen]


        