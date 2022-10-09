# 封装：将现实世界事物在类中描述为属性和方法
# 现实事物有部分属性和行为是不对使用者开放的，即私有成员
# 类对象无法访问私有成员
# 类中的其他成员可以访问私有成员

# 定义一个类，内含私有成员变量和私有成员方法（__开头的变量和方法）


class Phone:
    __current_voltage = 1  # 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核模式运行进行省电")


phone = Phone()
# print(phone.__current_voltage)
# phone.__keep_single_core()
phone.call_by_5g()
