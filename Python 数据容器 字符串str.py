# 字符串 基本操作
# 特点：不可变性、有序性、可迭代性

s = "Hello-Python-Hello-World"

print(s[5]) # 正向索引
print(s[-1]) # 反向索引

# 字符串不可修改
# s[4] = "x"
# print(s[4])

for i in s:
    print(i)

# 切片
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])

# 步长 -->正数：从前往后截取；负数：从后往前截取
print(s[0:5:2])
print(s[-1:-7:-1]) # 反转字符串nohtyP
print(s[::-1])

# 字符串的方法
# find() 在字符串中查找字串，返回第一次出现的索引位置，找不到返回-1
print(s.find("P"))

# count() 统计子字符串在指定字符串中出现的次数
print(s.count("Hello"))

# upper() 转为大写
print(s.upper())

# lower() 转为小写
print(s.lower())

# split() 将字符串按照指定字符串切割 - 列表
print(s.split("-")) # ['Hell', '-Pyth', 'n-Hell', '-W', 'rld']
print(s.split("o")) # ['Hell', '-Pyth', 'n-Hell', '-W', 'rld']

# strip() 去除字符串两端的空白字符或指定字符
print(s)
print(s.strip())

# replace() 将字符串中的指定字串替换为新的字串
print(s.replace("H", "C"))

# startswith() 检查字符串是否指定子串开头，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))

print(s)
