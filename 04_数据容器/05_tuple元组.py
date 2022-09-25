# 元组跟列表list类似，[]->()且不能修改（所以list涉及修改的方法元组没有）,元组允许重复数据
# 定义元组
t1 = (1, "hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}, 内容是：{t1}")
print(f"t2的类型是：{type(t2)}, 内容是：{t2}")
print(f"t3的类型是：{type(t3)}, 内容是：{t3}")

# 定义单个元素的元组（记得加,）
t4 = ("hello",)
print(f"t4的类型是：{type(t4)}, 内容是：{t4}")

# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是：{type(t5)}, 内容是：{t5}")

# 下标索引去取出内容（中括号！！）
print(f"嵌套元组中取元素：{t5[1][2]}")

# 元组的操作：index查找
t6 = ("wow", "pretty", "python")
index = t6.index("pretty")
print(f"在元组t6中查找pretty，下标是：{index}")

# 元组的操作：count统计方法
t7 = ("wow", "pretty", "pretty", "pretty", "python")
num = t7.count("pretty")
print(f"在元组t7中统计pretty数量有：{num}")

# 元组的操作：len函数统计元组元素数量
t8 = ("wow", "pretty", "pretty", "pretty", "python")
num = len(t8)
print(f"t8元组中元素有：{num}个")

# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素：{t8[index]}")
    index += 1

print("-----for------")
# 元组的遍历：for
for element in t8:
    print(f"元组的元素：{element}")

# 特例！元组里面的list元素 里面的内容可以修改
t9 = (1, 2, ["hello", "world"])
print(f"t9的内容是：{t9}")
t9[2][0] = "你好"
t9[2][1] = "世界"
print(f"t9的内容是：{t9}")

