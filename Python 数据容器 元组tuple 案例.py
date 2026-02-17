"""
根据如下提供的学生成绩单，完成如下需求：
    1.计算每个学生的总分、各科平均分、然后一并输出出来
    2.统计各科成绩的最低分、最高分、平均分，并输出。
    3.查找成绩优秀（平均分 >= 90）的学生，并输出。
"""

student  = (
    ("S001", "王林", 80, 90, 70),
    ("S002", "李四", 60, 80, 90),
    ("S003", "张三", 80, 80, 80),
    ("S004", "赵六", 90, 90, 90),
    ("S005", "王五", 70, 70, 70),
    ("S006", "王小二", 80, 80, 80),
    ("S007", "王小三", 80, 80, 80),
    ("S008", "王小四", 80, 80, 80),
    ("S009", "王小五", 80, 80, 80),
    ("S010", "王小六", 80, 80, 80),
)
# 1.计算每个学生的总分、各科平均分、然后一并输出出来
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")

#方式一：
# for s in student:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")

#方式二：
for id,name,chinese,math,english in student:
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")

# 2.统计各科成绩的最低分、最高分、平均分，并输出。

# 2.1获取各科的成绩列表
chinese_scores = [chinese for s in student]
math_scores = [math for s in student]
english_scores = [english for s in student]
print("----------------------------------------------------------------------------------------------------------------")

#2.2 输出各科最低分、最高分、平均分
print(f"语文最低分",min(chinese_scores), "语文最高分",max(chinese_scores), "语文平均分",sum(chinese_scores) / len(chinese_scores))
print(f"数学最低分",min(math_scores), "数学最高分",max(math_scores), "数学平均分",sum(math_scores) / len(math_scores))
print(f"英语最低分",min(english_scores), "英语最高分",max(english_scores), "英语平均分",sum(english_scores) / len(english_scores))
print("----------------------------------------------------------------------------------------------------------------")

# 3.查找成绩优秀（平均分 >= 90）的学生，并输出。
print("优秀学生（平均分 >= 90）名单如下:")

# 方式1：
# for s in student:
#     avg = (s[2] + s[3] + s[4]) / 3
#     if avg > 90:
#         print(f"学号：{s[0]} 姓名：{s[1]} 平均分：{avg:.1f}")
#     else:
#         continue

# 方式2：
for id,name,chinese,math,english in student:
    avg = (chinese + math + english) / 3
    if avg >= 90:
        print(f"学号：{id} 姓名：{name} 平均分：{avg:.1f}")
    else:
        continue
