'''

#ch13_Disjoint Set

# 創建單元素集合
Make-Set(x)
x.p = x  # 初始化節點x的父節點為其自身
x.rank = 0  # 初始化節點x的秩為0

# 合併兩個集合，根據rank，rank是指深度
Link(x, y)
if x.rank > y.rank  # 如果x的秩大於y的秩
    y.p = x  # 將y的父節點設置為x
else  # 否則
    x.p = y  # 將x的父節點設置為y
    if x.rank == y.rank  # 如果x的秩等於y的秩
        y.rank = x.rank + 1  # 則增加y的秩

# 查找集合的根節點（帶路徑壓縮）
Find-Set(x)
if x ≠ x.p  # 如果x不是根節點
    x.p = Find-Set(x.p)  # 路徑壓縮：將x的父節點設置為根節點
return x.p  # 返回根節點

# 合併兩個集合
Union(x, y)
Link(Find-Set(x), Find-Set(y))  # 先找到x和y的根節點，再合併這兩個集合

#簡介：把同一個set的字串連在一起
#時間複雜度：O(m乘以a(n))

'''