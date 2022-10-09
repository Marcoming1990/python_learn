"""
    除了__init__构造方法是内置方法以外，还有以下内置方法（格式__xx__）
    __str__：类对象转字符串
    __lt__：2个类对象进行 小于或大于比较
    __le__：2个类对象进行 小于等于或大于等于比较
    __eq__：2个类对象进行 相等比较
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__内置方法（print打印的不再是内存地址，而是return内容）
    def __str__(self):
        return f"Student类对象，name:{self.name},age:{self.age}"

    # __lt__内置方法（<或者>都可以比较）
    def __lt__(self, other):
        return self.age < other.age

    # __le__内置方法（<=或者>=都可以比较）
    def __le__(self, other):
        return self.age <= other.age

    # __eq__内置方法（==比较运算符，没实现eq方法时比较的是内存地址）
    def __eq__(self, other):
        return self.age == other.age


print("__str__:")
stu1 = Student("周杰轮", 31)
print(stu1)
print(str(stu1))
print("__lt__:")
stu2 = Student("林俊杰", 35)
print(stu1 < stu2)
print(stu1 > stu2)
print("__le__:")
print(stu1 <= stu2)
print(stu1 >= stu2)
print("__eq__:")
print(stu1 == stu2)

