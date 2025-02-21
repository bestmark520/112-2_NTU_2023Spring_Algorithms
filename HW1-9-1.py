def longest_palindromic_substring_DP(s):
    # 找出最長迴文子字串的函式
    n = len(s)
    dp = [[False] * n for _ in range(n)]  # 畫出[n x n]動態規劃表格
    max_len = 1  # 最長迴文子字串的初始長度為1

    for i in range(n):
        dp[i][i] = True  # 單個字元本身就是迴文
    print("一開始動態規劃表格：")
    for row in dp:
        print(row)

    start = 0
    for length in range(2, n + 1):  # 遍歷不同長度的子字串
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                dp[i][j] = s[i] == s[j]  # 長度為2的子字串是否迴文的判斷
            else:
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])  # 根據前一個子字串的結果判斷是否迴文
            if dp[i][j] and length > max_len:
                max_len = length
                start = i  # 更新最長迴文子字串的起始索引

    # 輸出動態規劃表格和最長迴文子字串的長度
    print("動態規劃表格：")
    for row in dp:
        print(row)
    print("最長迴文子字串的長度：", max_len)
    return max_len

# 使用範例：
input_str = ("rotators")
result = longest_palindromic_substring_DP(input_str)