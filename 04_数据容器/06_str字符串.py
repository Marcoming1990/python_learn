my_str = "hello world!"
# 通过下标索引取值
value1 = my_str[1]
value2 = my_str[-11]
print(value1)
print(value2)
# 字符串跟元组一样是不能修改的，只能改成一个新的字符串
# my_str[1] = "E"  报错

# index方法
value = my_str.index("wo")
print(f"在字符串{my_str}中查找wo,其起始下标是：{value}")

# replace方法（替换，最后得到一个新的字符串）
new_my_str = my_str.replace("l", "L")
print(f"my_str没有改变：{my_str}")
print(f"new_my_str的值是：{new_my_str}")

# split方法（分割，同样得到一个新的列表对象）
my_str = "hello python hi world"
my_str_list = my_str.split(" ")  # 通过空格分割
print(f"字符串{my_str}空格分割后得到：{my_str_list},类型是{type(my_str_list)}")

# strip方法1（规整，去除前后空格和回车\n）
my_str = "   hello and hi   "
new_my_str = my_str.strip()
print(f"字符串{my_str}被strip后：{new_my_str}")

# strip方法2（规整，去除前后指定字符串）
my_str = "12hello and hi21"
new_my_str = my_str.strip("12")  # 1跟2 都会去掉
print(f"字符串{my_str}被strip('12')后：{new_my_str}")

# count方法（统计字符串中某字符串出现的次数）
my_str = "mybaby is mylove"
count = my_str.count("my")
print(f"字符串{my_str}中my出现的次数是：{count}")

# len方法（统计字符串的长度）
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")

