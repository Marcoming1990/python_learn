mylist = ["wow", "pretty", "python"]
# 1、查找某元素在列表内的下标索引
index = mylist.index("pretty")
print(f"pretty在列表中的下标索引是：{index}")

# 2、修改特定下标索引的值
mylist[0] = "哇"
print(f"列表wow元素改为哇：{mylist}")

# 3、在指定下标位置插入新元素
mylist.insert(1, "best")
print(f"列表第二个位置插入新元素best：{mylist}")

# 4、在列表的尾部追加 单个 新元素
mylist.append("2022")
print(f"列表最后追加单个新元素：{mylist}")

# 5、在列表的尾部追加 一批 新元素
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"列表最后追加一个新列表：{mylist}")

# 6、删除指定下标索引的元素（2种方式）
# 6.1 方式1：del 列表[下标]
mylist = ["wow", "pretty", "python"]
del mylist[2]
print(f"列表删除元素后：{mylist}")
# 6.2 方式2：列表.pop(下标)
mylist = ["wow", "pretty", "python"]
element = mylist.pop(2)
print(f"通过pop方法取出元素后：{mylist},取出的元素是：{element}")

# 7、删除某元素在列表中的第一个匹配项
mylist = ["wow", "pretty", "wow", "pretty", "python"]
mylist.remove("pretty")
print(f"通过remove方法移除元素后：{mylist}")

# 8、清空列表
mylist.clear()
print(f"列表被清空了：{mylist}")

# 9、统计列表内某元素的数量
mylist = ["wow", "pretty", "wow", "pretty", "python"]
count = mylist.count("pretty")
print(f"列表中pretty的数量是：{count}")

# 10、统计列表中全部的元素数量
mylist = ["wow", "pretty", "wow", "pretty", "python"]
count = len(mylist)
print(f"列表的元素数量总共：{count}个")
