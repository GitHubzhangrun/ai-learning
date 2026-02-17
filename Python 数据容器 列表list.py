"""
此案例讲解列表操作

列表是数据容器中的一类，一次性可以存储多个数据（元素）的，每个元素可以是一个数据类型。

特点：
可以存储不同类型的元素（下标，索引（从前到后（正向索引），下标从0开始；从后向前（反向索引），下标从-1开始））
元素有序、可以重复、可以修改

序列类型：容器中的元素按特定顺序排列的，可通过索引访问的容器类型称之为序列
注意：从前到后（正向索引），下标从0开始；从后向前（反向索引），下标从-1开始）
"""

# 定义列表
s_list = [1,2,3,"A","start",False]

# 访问列表元素
# 获取
print(s_list[0]) #正向索引 从0开始
print(s_list[-6]) #反向索引 从-1开始

# 修改
s_list[3] =  "ABC"
print(s_list)

# 注意如果指定的索引超出范围，将会报错list assignment index out of range
# s_list[10] = "DEF"  # 超出
# print(s_list)

# 删除
del s_list[4]
print(s_list)

# for循环遍历打印
for x in s_list:
    print(x)

# 列表 -切片
# 语法：s_list[始索引（默认0）：结束索引（默认列表长度）：步长（默认1）]

print(s_list[0:5:1]) # 开始索引：结束索引：步长，默认1
print(s_list[:5]) # 简化 第一个：不能省略
print(s_list[0:5:2])
print(s_list[0:-2:1])



# 列表 -常见方法
# 调用操作

# 在列表尾部追加元素
s_list.append(666)
print(s_list)

# 在指定元素之前，插入该元素
s_list.insert(0,"A")
print(s_list)

# 移除列表中第一个匹配到的值
s_list.remove("A")
print(s_list)

# 删除列表中指定索引位置的元素（如果未指定索引，默认删除最后一个）
s_list.pop(4)
print(s_list)
s_list.pop()
print(s_list)

# 对列表进行排序（列表元素的数据类型一致，才可以进行排序）
s_list.insert(3,2)
print(s_list)
# s_list.sort() #列表元素的数据类型一致，才可以进行排序
# print(s_list)

# 反转列表元素
s_list.reverse()
print(s_list)