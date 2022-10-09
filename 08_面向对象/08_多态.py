"""
    多态：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
    抽象类：含有抽象方法的类（父类确定有哪些方法，具体实现由子类自行决定）
    抽象方法：方法体是空实现的（pass）
"""


class Animal:  # 抽象类（不工作，相当于顶层设计或者标准，也是对子类的软性约束，要求子类必须复写（实现）父类的一些方法）
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    # 制造点噪音，需要传入Animal对象
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)
