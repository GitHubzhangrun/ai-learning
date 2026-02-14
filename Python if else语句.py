"""
演示if else组合判断语句
"""
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age = int(input("请输入您的年龄："))
if age >= 18:
     print("您已成年，游玩需要补票10元。")
else:
     print("您未成年，可以免费游玩。")
print("祝您旅途愉快！")


print("欢迎来到黑马动物园。")
height = int(input("请输入您的身高（cm）："))
# 通过if进行判断
if height >120:
    print("您的升高超出120cm，游玩需要购票10元。")
else:
    print("祝您游玩愉快。")