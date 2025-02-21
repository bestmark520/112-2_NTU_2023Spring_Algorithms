#DP走路問題，可以走或跳，如果遇到障礙物就一定要跳
def min_energy(n, obstacles):
    dp = [float('inf')] * (n + 1) #創建一個長度為 n+1 的動態規劃數組 dp
    # 並初始化每個位置為正無窮，表示初始狀態下到達該位置的能量為無窮大（即無法到達）
    dp[0] = 0 #起始位置的能量消耗為 0

    for i in range(1, n + 1): #從位置1開始，遍歷到位置，
    #人先走到i的位置，再考慮從i-1跳過來還是i-4跳過來
        if i - 1 not in obstacles:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        if i - 4 >= 0 and i - 4 not in obstacles:
            dp[i] = min(dp[i], dp[i - 4] + 6) #這邊的dp[i]是指可能用i-1方式一步步走過來，看從i-4走過來是否有更小的情況
        #從i-4走過來要花更多能量，所以這行只有在有障礙物時才有作用

        print(f'i is {i},dp is {dp[i]}')

    return dp[n]

# 示例用法
n = 6
#obstacles = [3, 5, 9]
#obstacles = [1] #如障礙物設在1，那位子2、位子3都不可能達到，如print所示，但位子4就可以達到，從位子0跳過去
obstacles = [1]
min_energy_required = min_energy(n, set(obstacles))
print(f"最小所需能量為: {min_energy_required}")