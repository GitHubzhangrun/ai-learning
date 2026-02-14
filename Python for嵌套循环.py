# 坚持表白100天，每天都送10多花
#
# # # 定义天数
# i = 0
#
# # for外层循环，坚持表白100天
# for i in range(1,101):
#     print(  f"今天是向小美表白的第{i}天，加油坚持！")
#
#     #内层循环，每天栋送10多玫瑰花
#     for j in range(1,11):
#         print(f"给小美送的第{j}多玫瑰花")
#     print("小美我喜欢你！")
#
# print(f"第{i}天，表白成功了")



# for循环实现九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}\t", end='')

    # 外层循环可以通过print输出一个回车符
    print()
