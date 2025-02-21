def SCS(str1: str, str2: str) -> str:
    # 生資導dp圖畫出格子
    m, n = len(str1), len(str2)
    dp = [[""] * (n + 1) for _ in range(m + 1)]

    # 填充dp數組，就是畫生資導DP圖
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            #dp[i][j] = (dp[i - 1][j - 1] + str1[i - 1]) if str1[i - 1] == str2[j - 1] else max(dp[i - 1][j], dp[i][j - 1], key=len)
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + str1[i - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

    # 輸出SCS
    i, j = 0, 0
    res = ""
    for c in dp[m][n]:
        while i < m and str1[i] != c:
            res += str1[i]
            i += 1
        while j < n and str2[j] != c:
            res += str2[j]
            j += 1
        res += c
        i += 1
        j += 1

    return res + str1[i:] + str2[j:]

# 示例用法
result = SCS("ATCGT", "TGACG")
print(result)  # Output: "TGATCGT"