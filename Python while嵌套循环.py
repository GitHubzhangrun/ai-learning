# """
# while嵌套循环
# 同判断语句的嵌套一样，循环语句的嵌套，要注意空格缩进。
# *基于空格缩进来界定层次关系
# 注意条件的设置，避免出现无限循环（除非真的需要无限循环）
# """
#
#
# # 记录表白天数
# i = 0
#
# while i < 100:
#     i += 1
#     print(f"今天是第{i}天表白")
#     # 内层循环控制变量
#     j = 0
#     # 记录总共送出多少支玫瑰花
#     count = 0
#     while j < 10:
#         j += 1
#         count += 10
#         print(f"送了小美{j}朵玫瑰")
#
# print(f"在第{i}天表白，一共送了{count}朵玫瑰花，我成功了")


# # 案例：用while嵌套循环实现九九乘法表
# print("hello",end='')
# # print("world",end='')
# print("ITheima\tworld")
# print("hello\tworld")

# 定义外层循环的控制变量 行数
i = 1
while i <= 9:

    # 定义内层循环的控制变量 列数
    j = 1
    while j <= i:
        # 内层循环的print语句，不要换行，通过\t制表符进行对齐
        print(f"{j} * {i} = {j * i}\t",end='')
        j += 1

    i += 1
    print() # print空内容，就是输出一个换行


