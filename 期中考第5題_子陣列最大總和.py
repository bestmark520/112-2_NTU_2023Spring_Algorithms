'''
題目：Leetcode53 Maximum Subarray
在一個整數陣列中，找出「連續」子陣列，使得總和最大，並回傳這個最大總和。
'''

def max_subarray_sum_violent(nums):  # 方法一：雙層迴圈暴力解 # 複雜度O(n^2)
    results_max = nums[0]  # 初始化為第一個元素（避免全負數出錯）
    start = end = 0  # 紀錄最大子陣列的起始與結束位置

    for i in range(len(nums)):
        process = 0  # 每次從新的起點重新累加
        for j in range(i, len(nums)):
            process += nums[j]  # 累加從 i 到 j 的總和

            # 如果目前累加結果大於歷史最大值，就更新
            if process > results_max:
                results_max = process
                start = i
                end = j + 1  # Python 切片右邊要 +1

    max_seq = nums[start:end]  # 取得最大連續子陣列
    print(f"最大連續數列為 {max_seq}，總和為 {results_max}")
    return results_max

def max_subarray_sum(nums):  # 方法二：Kadane 演算法 # 複雜度O(n)
    max_sum = nums[0]  # 初始化最大總和
    current_sum = nums[0]  # 當前累積總和

    start = end = 0  # 最終最大子陣列的起始與結束索引
    temp_start = 0  # 暫存可能的起始索引

    for i in range(1, len(nums)):

        # 如果目前累積總和小於 0，代表會拖累後續總和
        # 直接從當前元素重新開始
        if current_sum < 0:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        # 如果發現更大的總和，才正式更新最大子陣列位置
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    max_subarray = nums[start:end + 1]
    print(f"最大連續數列為 {max_subarray}，總和為 {max_sum}")
    return max_sum, max_subarray

nums = [1, 2, 3, -5, 7, 8, -10, 2, 3, 4]
max_subarray_sum_violent(nums)
max_subarray_sum(nums)
