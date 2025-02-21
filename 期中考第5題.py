def max_subarray_sum_Jack(nums): #方法1，我想到的
    results_max = 0
    start = end = 0  # 记录最大子数组的起始位置和结束位置

    for i in range(0, len(nums)):
        process = 0
        for j in range(i, len(nums)):
            process += nums[j]
            #print(f'i is {i}, j is {j}, process is {process}')
            if process > results_max:
                results_max = process
                start = i  # 更新最大子数组的起始位置
                end = j+1  # 更新最大子数组的结束位置
                #print(f'start is {start}, end is {end}, process is {process}')

    max_seq = nums[start:end]  # 最大子数组
    print(f"最大連續數列為 {max_seq}, 總和為 {results_max}")
    return results_max

def max_subarray_sum(nums): #方法2，Kadane 算法
    max_sum = nums[0]  # 初始化最大和為第一個元素
    current_sum = nums[0]  # 當前和也為第一個元素
    start = 0  # 最大子數列起始索引
    end = 0  # 最大子數列結束索引

    for i in range(1, len(nums)):
        # 如果當前和小於0,則重置當前和為當前元素
        if current_sum < 0:
            current_sum = nums[i]
            start = i  # 更新起始索引
        else:
            current_sum += nums[i]

        # 更新最大和及結束索引
        if current_sum > max_sum:
            max_sum = current_sum
            end = i

    # 構造最大子數列
    max_subarray = nums[start:end + 1]
    print(f"最大連續數列為 {max_subarray}, 總和為 {max_sum}")
    return max_sum, max_subarray

nums = [1, 2, 3, -5, 7, 8, -10, 2, 3, 4]
max_subarray_sum_Jack(nums)
max_subarray_sum(nums)