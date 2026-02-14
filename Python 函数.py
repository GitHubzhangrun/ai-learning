"""
为什么学习使用函数呢？
为了得到一个针对特定需求/可供重复利用的代码段
提高程序的复用性，减少重复性代码，提高开发效率

已组织好的,可重复使用的，用来实现特定功能的代码段

注意事项：
参数/返回值不需要，可以省略

函数的定义：
def 函数名（传入参数）
    函数体
    return 返回值
"""

# # 定义一个函数，输出相关信息
# def say_hello(): #没有参数
#     print("hello")
#
# # 调用函数，让定义的函数去工作
# say_hello()


# def main():
#     print("欢迎来到黑马程序员！")
#     print("请出示您的健康码和72小时核酸证明！")
#
# main()
#

# 函数的传入参数
# # 定义一个两数相加的函数，通过参数接收被计算的2个数字
# def add(x,y):
#     result = x + y
#     print(f"{x} + {y} = {result}")
#
# # 调用参数，传入参数，传入的时候按照顺序传入，使用逗号分隔
# add(1,2)


# def main(x):
#     if x <= 37.5:
#         print(f"您的体温是{x}度，正常请进")
#     else:
#         print(f"您的体温是{x}度，需要隔离")
#
# main(37.2)
# main(37.9)


# 函数的返回值

def add(x,y):
    """
    add函数可以接收两个参数，进行2数相加的功能
    :param x: 相加的一个数字
    :param y: 相加的另一数字
    :return: 返回两数相加的结果
    """

    result = x + y
    # 通过返回值，遇到return，后面的程序都不会执行。
    return result
    # 返回结果后，还想输出一句话
    print("我完事了")

add(1,2)


# 特殊字面量：None 用在函数无返回值时
# 在if判断中，None等同于False
# 一般用于在函数中主动返回None，配合if判断做相关处理

# 无return返回值
def say_hello():


    print("Hello World")

result = say_hello()
print(f"无返回值函数时，返回的内容是：{result}")
print(f"无返回值函数时，返回的数据类型是：{type(result)}")

# 主动返回None的函数
def say_hello2():
    print("Hello World")

result = say_hello2()
print(f"无返回值函数时，返回的内容是：{result}")
print(f"无返回值函数时，返回的数据类型是：{type(result)}")

# None用于声明无初始内容的变量
name = None