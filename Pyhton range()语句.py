"""
range()语句,一般配合for循环使用

"""
#
# # 语法1：range(num) 从0开始到num-1，不含num本身
# for x in range(10):
#     # 从0开始到10结束，不包含10
#     print(x)
#
# # 语法2：range(num1,num2)
# for x in range(5,10):
#     # 从5开始到10结束，不包含10，步长是1
#     print(x)
#
# # 语法3：range(num1,num2,step)
# for x in range(1,10,2):
#     # 从1开始到10结束，不包含10，步长是2
#     print(x)

# 定义一个数字变量
num = 100
# 记录偶数出现个数,这个一定要在for循环外边定义。
count = 0

#for循环去遍历1-num的序列
for i in range(1,num):
    #if判断是否为偶数
    if i % 2 == 0:
        count += 1

print(f"1到100（不含100）范围内，有{count}个偶数")
