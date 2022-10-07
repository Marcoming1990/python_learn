# return只会执行一个，执行后退出函数

# 演示使用多个变量，接收多个返回值
def test_return():
    return 1, "hello", True


x, y, z = test_return()
print(x)
print(y)
print(z)
