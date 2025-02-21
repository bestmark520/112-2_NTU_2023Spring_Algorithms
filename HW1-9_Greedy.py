#找有幾個對稱字
def longest_palindromic_substring_Greedy(s: str) -> int:
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if len(s) < 1:
        return 0

    max_length = 0
    for i in range(len(s)):
        len1 = expand_around_center(i, i)  # 以单个字符为中心
        len2 = expand_around_center(i, i + 1)  # 以相邻两个字符为中心
        max_length = max(max_length, len1, len2)

    return max_length

# 示例用法
result = longest_palindromic_substring_Greedy("babad")
print(result)  # Output: 3
