"""
演示Python判断语句：if语句的基本格式应用
"""

age = 16
print(f"今年我{age}岁了")

if age >= 18:
    print("我今年成年了")
    print("即将步入大学生活！")

print("时间过的真快啊！")


# input获取键盘输入
age = int(input("请输入你的年龄："))
# age = int(age)
# 通过if判断是否是成年人
if age >= 18:
    print("您已成年，游玩需要补票10元。")
print("祝您游玩愉快。")


