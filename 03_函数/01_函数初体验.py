str1 = "hello"
str2 = "my"
str3 = "bro!"


# 定义函数，可以重复使用
# data是形参，str1 str2 str3是实参
# 其实这个函数也会有返回值，只是返回None而已，类型是<class 'NoneType'>
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是：{count}")


my_len(str1)
my_len(str2)
my_len(str3)


# 带返回值的函数
def add_str(s1, s2, s3):
    result = s1 + " " + s2 + " " + s3
    return result


str_all = add_str(str1, str2, str3)
print(str_all)
