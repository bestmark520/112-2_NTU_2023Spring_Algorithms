'''
題目：輸入只能是奇數個元素的nums，排序後 → 最大、最小、第二大、第二小… → 最後放中位數
輸入 2,3,4,1,5,7,6
輸出 7,1,6,2,5,3,4
'''

def order_sequence(seq):
    if len(seq) % 2 == 0: return # 檢查數列長度是否為奇數
    seq.sort()
    
    result = []
    left = 0
    right = len(seq) - 1
    while left < right:
        result.append(seq[right])
        result.append(seq[left])
        right -= 1
        left += 1

    result.append(seq[left]) # 將中間數字放到最後
    return result

input_seq = [2, 3, 4, 1, 5, 7, 6]
print(order_sequence(input_seq))

'''
- 輸入只能是奇數個數列，否則回傳錯誤
- 先將數列由小到大排序
- 用迴圈將
    - 第一個數字是最大的數字，
    - 第二個數字是最小的數字，
    - 第三個數字是第二大的數字，
    - 第四個數字是第二小的數字，
    - 以此類推
- 最後剩下一個數字，最中間的數字放到最後一個
'''
