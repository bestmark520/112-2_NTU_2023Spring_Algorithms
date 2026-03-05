def longest_palindromic_substring_Greedy(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if len(s) < 1: return 0

    max_length = 0
    for i in range(len(s)):
        len1 = expand_around_center(i, i)  # 以單字為中心
        len2 = expand_around_center(i, i + 1)  # 以相鄰兩個字為中心
        max_length = max(max_length, len1, len2)

    return max_length

print(longest_palindromic_substring_Greedy("babad")) # Output: 3
