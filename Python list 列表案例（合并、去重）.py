# """
# 案例1：将用户输入的10个数字存入列表中，并进行排序，输出最小值、最大值、平均值
#
# """
# # 1.定义一个空列表
# num_list = []
#
# # 2.将用户输入的10个数字存入列表
# for i in range(10): #range（10）10次
#     num = int(input("请输入一个有效的数字："))
#     num_list.append(num)
#
# print("数字列表：", num_list)
#
# # 3.列表元素排序
# num_list.sort()
# print("排序后的数字列表：", num_list)
#
# # 4.输出最小值、最大值、平均值 --->sun()求和、len()获取元素个数（列表长度）、min()获取最小值 、max()获取最大值
# print("最小值", num_list[0])
# #print("最小值", min(num_list))
# print("最大值", num_list[-1])
# #print("最大值", max(num_list))
# print("平均值", sum(num_list)/len(num_list))



# # 案例2：合并两个列表的元素，并将合并的结果进行去重处理（去除列表的重复元素）
#
# # 定义列表
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1.合并列表
# for num in num_list2:
#     num_list1.append(num)
#
# print("合并后的原始列表为：", num_list1)
#
# # 2.去重复记录
# new_list = [] #去除重复记录的列表
#
# for num in num_list1:
#     # 判断new_list中否存在num元素，如果不存在，再追加
#     if num not in new_list: # 判断元素是否存在于列表中，如果存在，则返回True；不存在，返回False
#         new_list.append(num)
#
# print("合并去重后的列表为：",new_list)


# # 案例2（简化）：合并两个列表的元素，并将合并的结果进行去重处理（去除列表的重复元素）
#
# # 定义列表
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1.合并列表
# # 解包：将列表这一类容器解开成一个一个单独的元素
# # 组包：将一个一个单独的元素合并到一个容器
# num_list = [*num_list1, *num_list2]
#
# print("合并后的原始列表为：", num_list)
#
# # 2.去重复记录
# new_list = [] #去除重复记录的列表
#
# for num in num_list:
#     # 判断new_list中否存在num元素，如果不存在，再追加
#     if num not in new_list: # 判断元素是否存在于列表中，如果存在，则返回True；不存在，返回False
#         new_list.append(num)
#
# print("合并去重后的列表为：",new_list)


# # 案例2（简化）：合并两个列表的元素，并将合并的结果进行去重处理（去除列表的重复元素）
#
# # 定义列表
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1.合并列表
# num_list = num_list1 + num_list2
# print("合并后的原始列表为：", num_list)
#
# # 2.去重复记录
# new_list = [] #去除重复记录的列表
#
# for num in num_list:
#     # 判断new_list中否存在num元素，如果不存在，再追加
#     if num not in new_list: # 判断元素是否存在于列表中，如果存在，则返回True；不存在，返回False
#         new_list.append(num)
#
# print("合并去重后的列表为：",new_list)





