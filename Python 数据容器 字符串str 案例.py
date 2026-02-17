"""
案例1：邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.）,如果输入正确，输出“邮箱格式正确”，否则输出“邮箱格式错误”
"""
#
# # 方式1：count（）
# # 1、接受用户输入的邮箱
# mail = input("请输入一个邮箱：")
#
# # 2、判断邮箱的格式
# if mail.count("@") == 1 and mail.count(".") >= 1:
#     print("您输入的邮箱正确:", mail)
# else:
#     print("您输入的邮箱错误:", mail)

# # 方式2：in 运算符 ---> 判断字串是否在字符串中，存在，返回True；不存在，返回False
# # 1、接受用户输入的邮箱
# mail = input("请输入一个邮箱：")
#
# # 2、判断邮箱的格式
# if mail.count("@") == 1 and "." in mail:
#     print("您输入的邮箱正确:", mail)
# else:
#     print("您输入的邮箱错误:", mail)


# 案例2：输入一个字符串，判断该字符串是否是回文（两边对称）
# 黄山落叶松叶落山黄 上海自来水来自海上

# # 1、接受用户输入的字符串
# s = input("请输入一个字符串：")
#
# # 2、判断是否是回文
# new_s = s[::-1] # 反转字符串
# if s == new_s:
#     print(f"您输入的字符串{s}是回文")
# else:
#     print(f"您输入的字符串{s}不是回文")

# # 案例3：将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来
#
# # 定义列表
# new_list = []
#
# # 输入10个字符串
# for s in range(1,11):
#     string = str(input("请输入一个字符串："))
#     string = string[::-1] # 字符串不可修改，必须将修改后的值重新赋值回变量
#     string = string.upper()  # 字符串不可修改，必须将修改后的值重新赋值回变量
#     new_list.append(string)
#
# print(new_list)
#
# # 遍历输出
# for s in new_list:
#     print(s)

# 案例3（简化）：将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来

# 定义列表
new_list = []

# 输入10个字符串
for s in range(1,11):
    string = str(input("请输入一个字符串："))[::-1].upper() #将反转、转大写可以写在一行。
    new_list.append(string)

print(new_list)

# 遍历输出
for s in new_list:
    print(s)


