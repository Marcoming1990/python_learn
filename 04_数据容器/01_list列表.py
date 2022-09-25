# list列表
# 元素数据类型没有限制
my_list = ['字符串', 666, True]
print(my_list)
print(type(my_list))

# 嵌套列表
my_list1 = [[1, 2, 3], [4, 5, 6]]
print(my_list1)
print(type(my_list1))

print("-----正向索引-----")
# 下标索引（正向）
print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[3])  下标超出范围会报错
print("-----反向索引-----")
# 下标索引（反向）
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

print("-----嵌套元素-----")
# 取出嵌套列表的元素
print(my_list1[0][0])
print(my_list1[0][1])
print(my_list1[1][1])
