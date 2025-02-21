#SCS問題，補充在演算法word檔，這是錯的程式
def shortestCommonSupersequence(str1: str, str2: str) -> str:
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化base cases
    for i in range(m + 1):
        dp[i][0] = i  #設定x軸是數列X
    for j in range(n + 1):
        dp[0][j] = j  #設定y軸是數列Y

    # 填充dp數組，就是畫生資導DP圖
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    # 輸出SCS
    i, j = m, n
    res = ""
    while i > 0 and j > 0:
        print(f'{str1[i - 1]},{str2[j - 1]}')
        if str1[i - 1] == str2[j - 1]:  #往右下角走 #此時是word檔中例題的紅框
            res = str1[i - 1] + res
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] < dp[i][j - 1]:  #往下面走，↓，輸出y軸的答案
                res = str1[i - 1] + res
                i -= 1
            else:
                res = str2[j - 1] + res  #往右邊走，→，輸出x軸的答案
                j -= 1

    return res + str1[:i] + str2[:j]

'''
    # LCS，比較跟SCS的差異
    i, j = m, n
    lcs = ""
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs
'''

# 示例用法
result = shortestCommonSupersequence("GTCA", "GTACG")
result = shortestCommonSupersequence("ATCGT", "TGACG")
print(result)