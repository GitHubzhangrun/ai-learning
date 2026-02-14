# 1、字符串在Python中的多种定义方式
# 单引号定义法，使用单引号进行包围
name = '黑马程序员'
print(type(name))
# 双引号定义法
name = "黑马程序员"
print(type(name))
# 多引号定义法
name = """
我是
黑马
程序员
"""
print(type(name))

# 在字符串内，包含双引号
name = '"黑马程序员"'
print(name)
# 在字符串内，包含单引号
name = "'黑马程序员'"
print(name)
# 引号嵌套，使用转移字符\,使得引号定义字符串失去效用
name = ("\"黑马程序员\"")
print(name)
name = ('\'黑马程序员\'')
print(name)




# 2、字符串拼接：字面量+字面量（没有实际意义），字面量+变量 ，变量+变量
# 使用"+"号连接字符串变量或字符串字面量即可
# 无法与非字符串类型进行拼接
#字面量+变量拼接
name = "张润"
address = "西安市东新街240号"
tel = 18092124665
print("我叫："+ name,"我的地址是："+ address,"我的电话："+ str(tel))

# 3、字符串格式化
# 问题：1、变量过多，拼接太麻烦；2、字符串无法与数字或其他数据类型完成拼接
# 多个变量去占位，变量要用括号括起来，并按照占位的顺序填入

# 通过占位的形式，完成拼接
massage = ("我是%s,住在%s,电话%s" % (name,address,tel))
print(massage)

# 通过占位的形式，完成数字和字符串的拼接
name = "黑马程序员"
num = 150
massage1 = ("%s第一期学员一共有%s人" % (name,num))
print(massage1)

# 4、字符串精度控制
num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d"  % num1)
print("数字11宽度限制1，结果是：%1d" % num1)  #m比数字本身宽度小，m不生效
print("数字11.345宽度限制7，小数精度限制2，结果是：%7.2f" % num2)  #注意宽度没有d
print("数字11.345宽度不限制，小数精度限制2，结果是：%.2f" % num2)  #小数做四舍五入

#5、字符串格式化快速写法 ，f {变量} {变量}
#  特点：1、不理会类型 2，不做精度控制，适合对精度没有要求的时候快速使用
name = "世茂集团"
set_up_year = 1996
stock_price = 19.99
# f：fomot  格式化的首字母
print(f"我是{name},我成立于{set_up_year}，我今天的股票价格是{stock_price}元")

#6、对表达式进行格式化
# 表达式：1条具有明确执行结果的代码语句
# 在无需使用变量进行数据存储的时候，可以直接格式化表达式，简化代码
print("1 * 1的结果是：%d" % (1*1))
print(f"1 * 1的结果是：{1*1}")
print("字符串在Python中的类型名是：%s",type(1*1))


# 7、字符串格式化练习题
name = "传智博客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}元")
print("每日增长系数是：%.1f，经过%d天增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))

