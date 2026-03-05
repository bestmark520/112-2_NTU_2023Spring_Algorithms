# DP走路問題，每次可以走一步消耗1能量，或是跳四步消耗6能量，障礙物一定要用跳的方式經過
# n = 路徑有0~n
# obstackes是障礙物的位子
# 輸出最低花費的能量

def min_energy(n, obstacles):
    # 創建一個長度為 n+1 的動態規劃數組 dp
    # 初始化每個位置為正無窮，表示初始狀態下到達該位置的能量為無窮大（即無法到達）
    dp = [float('inf')] * (n + 1) 
    dp[0] = 0 # 初始條件 # 起始位置的能量消耗為 0

    for i in range(1, n + 1):
        # 分別取min(從i-1走過來還是i-4跳過來)
        if i - 1 not in obstacles: dp[i] = min(dp[i], dp[i - 1] + 1)
        # 從i-4走過來要花更多能量，所以只有在有障礙物時才用跳的
        if i - 4 >= 0 and i - 4 not in obstacles: dp[i] = min(dp[i], dp[i - 4] + 6) 
        print(f'i is {i},dp is {dp[i]}')
    return dp[n]

# 示例用法
n = 6
#obstacles = [3, 5, 9]
#obstacles = [1] # 如障礙物設在1，那位子2、位子3都不可能達到，但位子4就可以達到，從位子0跳過去
obstacles = [1]
min_energy_required = min_energy(n, set(obstacles))
print(f"最小所需能量為: {min_energy_required}")
