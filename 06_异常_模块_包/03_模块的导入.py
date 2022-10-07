# 模块名称就是文件的名称
# 导入time模块
import time  # 导入python内置的time模块（time.py这个代码文件）ctrl+左键 点击time可以进入文件

print("你好")
time.sleep(5)  # 睡眠五秒钟（.后面跟类、函数、变量）
print("我好")

# 导入time模块的sleep方法（函数）
# from time import sleep
# print("你好")
# sleep(5)  # 可以直接使用方法
# print("我好")

# * 导入time模块的全部功能（* 表示全部）
# from time import *
# print("你好")
# sleep(5)  # 可以直接使用方法
# print("我好")

# 使用as给特定功能加上别名
# import time as t
# print("你好")
# t.sleep(5)
# print("我好")

# from time import sleep as sl
# print("你好")
# sl(5)
# print("我好")
