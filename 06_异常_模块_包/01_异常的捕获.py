# 基本捕获语法
try:
    f = open("D:/python/project-learn/06_异常_模块_包/abc.txt", "r", encoding="UTF-8")
except:
    print("出现异常，文件不存在，open的r模式，改为w模式去打开")
    f = open("D:/python/project-learn/06_异常_模块_包/abc.txt", "w", encoding="UTF-8")

# 捕获指定的异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常
try:
    # 1 / 0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义的异常 或者 除以0的异常")

# 捕获所有异常（不像上面知道什么异常，那就捕获全部）
try:
    1 / 0
    # print(name)
    # print("hello")
except Exception as e:  # 顶级的异常 也可以只写except:
    print("有异常执行")  # 有异常执行
else:
    print("没异常执行")  # 没异常执行
finally:
    print("有没有异常都会执行！")  # 有没有异常都会执行
