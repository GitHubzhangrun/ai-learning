"""
演示while循环的基础应用
1、条件类型：结果必须是bool类型，true执行，false停止
2、终止条件：必须设置
3、书写格式：空格缩进
# """
from wsgiref.util import guess_scheme

# i = 0
# while i<5:
#     print("小美，我喜欢你！")
#     i += 1
#

# 案例：1-100求和
# sum = 0
# i = 1
# while i <= 100:
#     sum += i
#     i += 1
# print(f"1-100之和：", {sum})

# 案例：猜数字游戏

# 定义一个变量，记录总共猜的次数
count = 0
# 1-100内生成1个随机数
import random
num = random.randint(1,100)
#定义没猜中
flag = True

while flag:
    guess_num = int(input("请输入你要猜的数字："))
    count += 1
    if guess_num == num:
        print("你猜中了")
        flag = False
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")

print(f"你一共猜了{count}次")


