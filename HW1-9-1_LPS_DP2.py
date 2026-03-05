# 找出最長迴文子字串的函式
# leetcode 5

def longest_palindromic_substring_DP(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]  # 畫出 n x n 的 dp表格
    max_len = 1  # 最長迴文子字串的初始長度為1
    for i in range(n): dp[i][i] = True  # 單個字元本身就是迴文

    start = 0
    for length in range(2, n + 1):  # 長度
        for i in range(n - length + 1): # 起點
            
            j = i + length - 1
            
            # 長度為2的子字串是否迴文的判斷
            # dp[i][j] 會是 True 或 False
            if length == 2: dp[i][j] = s[i] == s[j]
            
            # 根據前一個子字串的結果判斷是否迴文
            # dp[i][j] 會是 True 或 False
            else: dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            
            if dp[i][j] and length > max_len:
                max_len = length
                start = i  # 更新最長迴文子字串的起始索引

    print("動態規劃表格：")
    for row in dp: print(row)
    print("最長迴文子字串的長度：", max_len)
    return max_len

longest_palindromic_substring_DP("rotators")
