# SCS = Shortest Common Supersequence 最短共同超序列
# 找一個最短字串：同時包含 str1, str2
# 有點像最小公倍數
# str1 = GTCA, str2 = GTACG, SCS 是 GTACAG 或 GTACGA

# LCS Longest Common Subsequence 最長共同子序列
# 兩個字串中：不用連續，但順序要一樣，找最長共同部分
# 有點像最小公因數
# str1 = "GTCA", str2 = "GTACG", LCS 是 G T C

# SCS長度 = m + n − LCS長度

def shortestCommonSupersequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化 # LCS不用初始化
    for i in range(m + 1): dp[i][0] = i  #設定x軸是數列X
    for j in range(n + 1): dp[0][j] = j  #設定y軸是數列Y

    # 填充dp數組，同生資導DP圖
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]: dp[i][j] = dp[i - 1][j - 1] + 1
            else: dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1 # 填寫DP的部分，SCS, LCS僅差在有沒有這行的 +1

    print("\nSCS DP Table:")
    print_dp_table(dp, str1, str2)

    # 輸出SCS
    # 回推 # 起點是dp[m][n]
    # 起點是dp[0][0]也可以，生資導起點是dp[0][0]
    i, j = m, n
    res = ""
    while i > 0 and j > 0:
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

def LCS(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 填DP表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]: dp[i][j] = dp[i - 1][j - 1] + 1
            else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print("\nLCS DP Table:")
    print_dp_table(dp, str1, str2)

    # 回推
    i, j = m, n
    lcs = ""

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]: i -= 1
        else: j -= 1
    return lcs

def print_dp_table(dp, str1, str2):
    m, n = len(str1), len(str2)

    print("    ", end="")
    print("  ".join([" "] + list(str2)))

    for i in range(m + 1):
        if i == 0:
            row_label = " "
        else:
            row_label = str1[i - 1]

        print(row_label, end="  ")

        for j in range(n + 1):
            print(dp[i][j], end="  ")
        print()

# 示例用法
print(shortestCommonSupersequence("GTCA", "GTACG"))
print(shortestCommonSupersequence("ATCGT", "TGACG"))
print(LCS("GTCA", "GTACG"))
print(LCS("ATCGT", "TGACG"))

'''
SCS DP Table:
      G  T  A  C  G
   0  1  2  3  4  5  
G  1  1  2  3  4  5  
T  2  2  2  3  4  5  
C  3  3  3  4  4  5  
A  4  4  4  4  5  6  
GTCACG

SCS DP Table:
      T  G  A  C  G
   0  1  2  3  4  5  
A  1  2  3  3  4  5  
T  2  2  3  4  5  6  
C  3  3  4  5  5  6  
G  4  4  4  5  6  6  
T  5  5  5  6  7  7  
TGACGTA

LCS DP Table:
      G  T  A  C  G
   0  0  0  0  0  0  
G  0  1  1  1  1  1  
T  0  1  2  2  2  2  
C  0  1  2  2  3  3  
A  0  1  2  3  3  3  
GTA

LCS DP Table:
      T  G  A  C  G
   0  0  0  0  0  0  
A  0  0  0  1  1  1  
T  0  1  1  1  1  1  
C  0  1  1  1  2  2  
G  0  1  2  2  2  3  
T  0  1  2  2  2  3  
TCG
'''
