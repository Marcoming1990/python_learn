# a模式文件不存在会创建，若存在会在最后追加写入文件
# 打开一个存在的文件
f = open("D:/python/project-learn/05_文件操作/test.txt", "a", encoding="UTF-8")
# write写入、flush刷新
f.write("\n追加：我是小红同学")
# close关闭
f.close()
