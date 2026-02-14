"""
演示Python的input语句
获取键盘的输入信息
"""

# print("请告诉我你是谁？")
name = input("请告诉我你是谁")
print("你是：%s" % name)

# 输入数字类型
num = input("你的银行卡号是：")
num = int(num)
print("我知道了，你的银行卡号是：%s" % type(num))

