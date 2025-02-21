#找有幾個對稱字
def longest_palindromic_substring_DP(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    max_length = 0

    # 初始化长度为1的回文子串
    for i in range(n):
        dp[i][i] = 1
        max_length = 1

    # 填充动态规划表
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                if l == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                max_length = max(max_length, dp[i][j])

    return max_length

# 示例用法
result = longest_palindromic_substring_DP("rotator")
print(result)  # Output: 3
