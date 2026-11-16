'''
Understanding the Problem:
- Input: We are given a string s.
- Goal: Find the length of the longest substring that contains no repeating characters.
- A substring must be continuous (characters must be next to each other).
- We only need to return the length, not the actual substring.

Constraints:
- The string can contain letters, digits, symbols, and spaces.
- The string can be empty.
- Characters must be unique within the substring.
- We need an efficient solution rather than checking every possible substring.

Examples:
1. Input: s = "abcabcbb"
   Output: 3
   Explanation: "abc" is the longest substring without repeating characters.

2. Input: s = "bbbbb"
   Output: 1
   Explanation: The longest valid substring is "b".

3. Input: s = "pwwkew"
   Output: 3
   Explanation: "wke" is the longest valid substring.
   Note: "pwke" is not a valid substring because its characters are not continuous.

Approach – Sliding Window + Set:
1. Initialize two pointers, left and right, to represent the current window.
2. Create a set to keep track of the characters currently inside the window.
3. Move the right pointer through the string, expanding the window by adding characters.
4. If the current character is already in the set:
   - Shrink the window from the left until the duplicate character is removed.
   - Remove each character from the set as the left pointer moves forward.
5. Add the current character to the set once it is no longer duplicated.
6. Calculate the current window length using right - left + 1.
7. Update the longest length whenever we find a larger valid window.
8. Return the longest length.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0 
        charset = set()
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            
            charset.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

