# 设计一个类（设计图纸）
class Student:
    # 成员变量
    name = None
    gender = None
    age = None

    # 成员方法 - def 方法名(self,形参1,形参2..):
    def say_hi(self):
        print(f"Hi大家好，我是{self.name}")
    # self表示类对象自身，定义时必须填写
    # 当使用类对象调用方法时，self会被python自动传入 stu_1 = Student()
    # 在方法内部，想要访问类的成员变量，必须使用self


# 创建一个对象（由图纸生产的具体实体）
stu_1 = Student()
# 对象属性进行赋值
stu_1.name = "小明"
stu_1.gender = "男"
stu_1.age = 31
# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.age)
stu_1.say_hi()

# 再创建另一个对象
stu_2 = Student()
# 对象属性进行赋值
stu_2.name = "小红"
stu_2.gender = "女"
stu_2.age = 25
# 获取对象中记录的信息
print(stu_2.name)
print(stu_2.gender)
print(stu_2.age)
stu_2.say_hi()
