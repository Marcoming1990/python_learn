# 例子1
# from my_module1 import test
#
# test(1, 2)

# 例子2
# from my_module1 import test  # 变灰色表示不会使用到
# from my_module2 import test  # 同方法，后面会覆盖前面
#
# test(1, 2)

# 例子3 - 在my_module1 加入了执行代码test()
# __main__变量
# from my_module1 import test  # 导入之后直接运行会得到5

# 例子4 - 在my_module1 if __name__ == '__main__':test(2, 3)
# __main__变量
# from my_module1 import test  # 导入之后直接运行没结果

# 例子5
# __all__变量
# * 表示全部，但是只能导入all定义过的内容
from my_module2 import *

# test(1, 2)   # 不能执行
test1(1, 2)  # 可以执行
