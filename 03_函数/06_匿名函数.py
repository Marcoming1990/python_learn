"""
def关键字，可以定义 带有名称 的函数
lambda关键字，可以 定义匿名 函数（无名称）
- 有名称的函数，可以基于名称重复使用
- 无名称的匿名函数，只可临时使用一次
"""


# 定义一个函数，接受其他函数输入
def test_func(compute):
    result = compute(1, 2)
    print(f"计算结果是：{result}")


# 通过lambda匿名函数的形式，将匿名函数作为参数传入
# lambda 传入参数： 函数体（只能一行代码）
test_func(lambda x, y: x + y)
