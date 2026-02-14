"""
continue 临时跳过本次循环，直接进入下一次循环，可以用于for或 while循环，效果一致
break 直接结束
"""

# # for循环 continue关键字应用
# for i in range(1, 5):
#     print("语句1")
#     continue
#     print("语句2")

# # for嵌套循环 continue关键字嵌套应用，只作用于当前循环层
# for i in range(1, 5):
#     print("语句1")
#     for j in range(1, 5):
#         print("语句2")
#         continue
#         print("语句3")
#
# print("语句4")

# 循环中断语句 break
# for i in range(1, 10):
#     print("语句1")
#     break
#     print("语句2")

# 循环嵌套中，中断语句break嵌套应用
for i in range(1, 3):
    print("语句1")
    for j in range(1, 3):
        print("语句2")
        break
        print("语句3")
    print("语句4")