"""
演示布尔类型的定义
比较运算符的应用
"""

# 定义变量存储布尔类型的值
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，数据类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}，数据类型是：{type(bool_2)}")

# 比较运算符的使用
# == != > < >= <=
# 演示相等/不相等比较
num1 = 20
num2 = 20
print(f"10 == 10的结果是：{num1 == num2}")

num1 = 10
num2 = 15
print(f"10 != 15的结果是：{num1 != num2}")

name1 = "itcast"
name2 = "itheima"
print(f"itcast == itheima的结果是：{name1 == name2}")

# 演示大于小于、大于等于/小于等于的比较运算
num1 = 10
num2 = 5
print(f"10 > 5的结果是：{num1 > num2}")
print(f"10 < 5的结果是：{num1 < num2}")

num1 = 10
num2 = 10
print(f"10 >= 10的结果是：{num1 >= num2}")
print(f"10 <= 10的结果是：{num1 <= num2}")




