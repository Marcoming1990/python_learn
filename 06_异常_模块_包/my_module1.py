def test(a, b):
    print(a + b)


# test(2, 3)

if __name__ == '__main__':  # 右键运行会把__name__变量的值设置为__main__，所以右键运行时候if为TRUE，执行代码
    test(2, 3)
# 说白了，if __name__ == '__main__'用于测试本文件代码，而不会被调用时候执行
