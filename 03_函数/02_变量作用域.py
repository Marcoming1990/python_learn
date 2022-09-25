num = 100


def testA():
    print(num)


def testB():
    num = 200  # 局部变量（跟外面的num没关系）
    print(num)


testA()
testB()
print(f"全局变量num = {num}")


def testC():
    global num  # 设置内部定义的变量为全局变量
    num = 300
    print(num)


testC()
