# list tuple str 都可以元素重复；set是不可重复（自带去重）且无序（所以无下标索引），允许修改
# 定义集合
my_set = {"hello", "and", "world", "and", "world"}
my_set_empty = set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")

# add方法 - 添加新元素
my_set.add("python")
my_set.add("hello")  # 重复不会加入
print(f"添加元素后：{my_set}")

# remove方法 - 移除元素
my_set.remove("hello")
print(f"移除元素后：{my_set}")

# pop方法 - 随机取出一个元素
my_set = {"hello", "and", "world"}
element = my_set.pop()
print(f"集合被取出元素是：{element},取出元素后：{my_set}")

# clear方法 - 清空集合
my_set.clear()
print(f"集合被清空：{my_set}")

# difference方法 - 取2个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)  # 1里面有但2没有的
print(f"取出差集后的结果是：{set3}")
print(f"取出差集后，原有set1没变：{set1}")
print(f"取出差集后，原有set2没变：{set2}")

# difference_update方法 - 消除2个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)  # 在1消除和2相同的元素
print(f"消除差集后，集合1结果：{set1}")
print(f"消除差集后，集合2结果：{set2}")

# union方法 - 2个集合合并为1个
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"2个集合合并结果：{set3}")
print(f"合并后，集合1没变：{set1}")
print(f"合并后，集合2没变：{set2}")

# len方法 - 统计集合元素数量
set1 = {1, 2, 3, 4, 5}
num = len(set1)
print(f"集合set1内元素数量有：{num}个")
set2 = {1, 2, 3, 4, 5, 2, 3, 4, 5}
num = len(set2)
print(f"集合set2内元素数量有：{num}个")  # 去重之后算数量

# 集合不支持下标索引，所以不支持while循环，但是可以for循环
# for - 集合的遍历
set1 = {1, 2, 3, 4, 5}
for ele in set1:
    print(f"集合元素有：{ele}")



