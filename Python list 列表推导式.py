# 案例3：生成1-20的平方列表

# 方式1：传统方式
num_list = []
# 遍历输出1-20的平方列表
for num in range(1, 21):
    num_list.append(num ** 2)
print("1-20的平方列表为：", num_list)

# 方式2：列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 ---> 语法格式1：要插入的值（可以是表达式或变量） for i in 序列/列表
num_list2 = [i**2 for i in range(1, 21)]
print("1-20的平方列表为：", num_list2)



#  案例4：从如下列表中提取所有偶数，并计算其平方，组成一个新的列表

num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72, 122]

# 方式1：传统方式
# 定义一个新的列表
new_list = []

for num in num_list:
    # 遍历判断元素是否为偶数，如果是，计算其平方，并追加到新的列表
    if num % 2 == 0:
        num = num * num
        new_list.append(num)

print("新的列表:", new_list)


# 方式2： 列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 ---> 语法格式2：要插入的值（可以是表达式或变量） for i in 序列/列表 if 条件判断
new_list2 = [i**2 for i in num_list if i % 2 == 0]


print("新的列表:", new_list2)