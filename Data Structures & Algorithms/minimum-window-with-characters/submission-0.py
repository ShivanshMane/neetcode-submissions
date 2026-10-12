'''
1) Understanding the problem = 
   Input = s, t two strings 
   Goal = Find the substring in s, such that every character in t
   Output = Return the shortest substring in s 

2) Constraints = what if s is empty, what if t is empty, s and t are same, including duplicates, what if len(s) < len(t)

3) Examples = s = "OUZODYXAZV", t = "XYZ" -> "YXAZ"
              s = "xyz", t = "xyz"        -> "xyz"
              s = "x", t = "xy"           -> ""
              s = "", t = "ABC"           -> ""
              s = "ADOBECODEBANC", t = "" -> ""

4) Brute Force Solution = generate all substrings of s, and count their frequencies and and check if it contains all the characters of t, if same return that particular substring 

'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        window = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0) 
        have, need = 0, len(countT)
        res, resLen = [-1, 1], float("infinity")
        l = 0 
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)    
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if ( r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else""      