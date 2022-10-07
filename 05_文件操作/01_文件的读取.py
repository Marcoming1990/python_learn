# open方法 - 打开文件

f = open("D:/python/project-learn/05_文件操作/文件读取测试.txt", "r", encoding="UTF-8")
print(type(f))

# read方法 - 读取文件
# print(f"读取10个字节的结果：{f.read(10)}")
print(f"读read方法读取全部内容：{f.read()}")  # 多次调用read，会继续读取

print("-----------------------------")
# readLines方法 - 读取文件
# lines = f.readlines()  # 读取文件的全部行，封装到列表中
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容：{lines}")

# readline方法 - 一次读取一行内容
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")

# for循环读取文件行
# for line in f:
#     print(f"每一行数据是：{line}")

# close - 文件的关闭
# f.close()

# with open - 语法操作文件（执行完时候会自动关闭close）
with open("D:/python/project-learn/05_文件操作/文件读取测试.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")
