# 打开一个不存在的文件，w:文件不存在会新建
f = open("D:/python/project-learn/05_文件操作/test.txt", "w", encoding="UTF-8")
# write - 写入（将内容写入到内存中）
f.write("hello world!!")
# flush - 刷新（将内存中积攒的内容，写入到硬盘的文件中）
f.flush()
# close - 关闭（close方法，内置了flush的功能
f.close()

# # 打开一个存在的文件，文件原有内容会被清空
# f = open("D:/python/project-learn/05_文件操作/test.txt", "w", encoding="UTF-8")
# # write写入
# f.write("我是小明")
# # close关闭
# f.close()
