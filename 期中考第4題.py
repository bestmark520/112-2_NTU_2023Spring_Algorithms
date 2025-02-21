def order_sequence(seq):
    # 檢查數列長度是否為奇數
    if len(seq) % 2 == 0:
        return "錯誤:輸入數列必須為奇數個數"

    # 將數列排序
    seq.sort()

    # 重新排列數列
    result = []
    left = len(seq) - 1
    right = 0
    while left > right:
        result.append(seq[left])
        result.append(seq[right])
        left -= 1
        right += 1

    # 將中間數字放到最後
    result.append(seq[right])
    return result

# 測試用例
input_seq = [2, 3, 4, 1, 5, 7, 6]
output = order_sequence(input_seq)
print(output)

'''
輸入只能是奇數個數列，否則回傳錯誤
1.先將數列由小到大排序
2.用迴圈將
第一個數字是最大的數字，
第二個數字是最小的數字，
第三個數字是第二大的數字，
第四個數字是第二小的數字，
以此類推
3.最後剩下一個數字，最中間的數字放到最後一個
===
輸入如 2,3,4,1,5,7,6
輸出為 7,1,6,2,5,3,4
'''