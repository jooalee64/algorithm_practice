"""
the problem involves finding the length of the longest 
substring in a given string, such that the substring contains
at most k distinct chars. 
for example string "abcba" k=2, return bcb
"""

def longest_substring_k_distinct(s,k):
    char_count = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right],0)+1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_len = max(max_len, right-left+1)
    return max_len

s = "abcba"
k = 2
result = longest_substring_k_distinct(s,k)
print(result)