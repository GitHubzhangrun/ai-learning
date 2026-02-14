"""
for循环与while循环的区别：
while循环的循环条件是自定义的，自行控制循环条件
for循环是一种 ”轮询“ 机制，是对一批内容进行 ”逐个处理“，通俗讲，就是将待办事项逐个处理，也可以叫做 “遍历循环”

所以理论上上讲，python中for循环无法构建无限循环（因为被处理的数据集无法无限大）
"""
# name = "itheima"
# #
# # for x in name:
# #     # 将name的内容，挨个取出赋予x临时变量
# #     # 就可以在循环体内对x进行处理
# #     print(x)
#
# # 统计如下字符串，有多少个a
# name = "itheima is a brand of itcast"
#
# # 定义次数累加
# count = 0
#
# # for循环统计
# for i in name:
#     if i == "a":
#         count += 1
# print(f"一共有{count}个英文字母：“a”")


# 演示pyhton for循环临时变量的作用域
# #要在for循环外访问临时变量，预先在循环前定义变量i
# i = 0
# for i in range(10):
#     print(i)
#
# print(i) #实际是可以访问变量i，但规范上不建议


# 坚持表白100天，每天都送10多花
