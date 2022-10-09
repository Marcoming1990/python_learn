# 复写：子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写
# 即：在子类中重新定义同名的属性或方法即可
# 复写后默认调用复写后的成员，若要调用父类 - 父类名.成员变量    父类名.成员方法


class Phone:
    IMEI = None  # 序列号
    producer = "美国"  # 厂商

    def call_by_5g(self):
        print("5g通话")


# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "中国"  # 复写父类的成员属性

    def call_by_5g(self):  # 复写父类的成员方法
        print("开启CPU单核模式，确保通话省电")
        # print("使用5g网络进行通话")

        # 调用父类的成员和方法（5g通话功能不用重新写）：
        # 方式1：
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        # 方式2：
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()

        print("关闭CPU单核模式，确保性能")


phone = MyPhone()
phone.call_by_5g()  # 优先调用复写成员
print(phone.producer)  # 优先调用复写成员

