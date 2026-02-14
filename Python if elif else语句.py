"""
演示 if elif else 多条件判断语句的使用
"""
# print("欢迎来到黑马动物园。")
# height = int(input("请输入您的身高（cm）："))
# vip_level = int(input("请输入你的VIP级别（1~5））"))
# # 通过if进行判断
# if height < 120:
#     print("您的升高小于120cm，可以免费游玩。")
# elif vip_level > 3:
#     print(f"您的VIP级别大于3,可以免费游玩。")
# else:
#     print("不好意思，您的条件都不满足，需要购票10元。")
# print("祝您游玩愉快。")
#
# # 猜猜心里数字
# num = 10
# if int(input("请输入第一次猜想的数字：")) == num:
#     print("恭喜你，第一次就猜对了！")
# elif int(input("猜错了，再猜一次：")) == num:
#     print("恭喜你，猜对了")
# elif int(input("猜错了，最后猜一次：")) == num:
#     print("恭喜你，最后一次猜对了")
# else:
#     print("不要意思，三次都猜错了。")
#
#
import random
num = random.randint(1,10)

guess_num = int(input("请输入你要猜测的数字："))
#通过if嵌套判断是否猜中
if guess_num == num:
    print("恭喜你第一次就猜中了")
else:
    if guess_num > num:
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")

    guess_num = int(input("请再次输入你要猜的数字"))
    if guess_num == num:
        print("恭喜你第二次猜中了")
    else:
        if guess_num > num:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")

        guess_num = int(input("请第三次输入你要猜的数字"))
        if guess_num == num:
            print("恭喜你，最后一次猜中了")
        else:
            print("不好意思，三次机会用完了")

