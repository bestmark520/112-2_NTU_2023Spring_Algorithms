#助教公布的解答，建立pre array，建立箭頭圖再輸出SCS
def shortestCommonSupersequence(str1: str, str2: str) -> str:
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    pre = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i + 2  # 初始化dp數組的x軸
        pre[i][0] = 3  # 初始化pre數組的x軸
    for j in range(n + 1):
        dp[0][j] = j + 2  # 初始化dp數組的y軸
        pre[0][j] = 2  # 初始化pre數組的y軸

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                pre[i][j] = 1
            else:
                if dp[i][j - 1] < dp[i - 1][j]:
                    dp[i][j] = dp[i][j - 1] + 1
                    pre[i][j] = 2
                else:
                    dp[i][j] = dp[i - 1][j] + 1
                    pre[i][j] = 3

    # 構建SCS
    i, j = m, n
    res = ""
    while i > 0 and j > 0:
        if pre[i][j] == 1:
            res = str1[i - 1] + res
            i -= 1
            j -= 1
        elif pre[i][j] == 2:
            res = str2[j - 1] + res
            j -= 1
        else:
            res = str1[i - 1] + res
            i -= 1

    while i > 0:
        res = str1[i - 1] + res
        i -= 1
    while j > 0:
        res = str2[j - 1] + res
        j -= 1

    return res

result = shortestCommonSupersequence("ATCGT", "TGACG")
print(result)