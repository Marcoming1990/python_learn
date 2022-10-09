# Python类可以使用: __init__()方法，称之为构造方法
# - 在创建类对象（构建类）的时候，会自动执行
# - 在创建类对象（构建类）的时候，将传入参数自动递给__init__方法使用


class Student:
    # 可以省略，因为下面有了
    # name = None
    # gender = None
    # age = None

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print("Studert类创建了一个对象")


stu = Student("周杰轮", "男", 31)
print(stu.name)
print(stu.gender)
print(stu.age)
