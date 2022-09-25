# 获取键盘的输入信息
name = input("你叫什么名字？")
print("我的名字叫：%s" % name)

# 输入数字类型
num = input("你多少岁？")
# 数据类型转换
num = int(num)
print("你的年纪的类型是：", type(num))

# 结论：input默认是str,需要其他类型需要转换
