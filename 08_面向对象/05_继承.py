# 单继承：class 类名(父类名):
# 多继承：class 类名(父类1,父类2,..):
# pass补全语法


class Phone:
    IMEI = None  # 序列号
    producer = "HM"  # 厂商

    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = "10001"  # 面部识别ID

    def call_by_5g(self):
        print("5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

print("------------多继承------------")


class NFCReader:
    nfc_type = "NFC第五代"
    producer = "XX"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")


class MyPhone(Phone2022, NFCReader, RemoteControl):
    # 不需要新增代码，那就用pass补全语法
    pass


phone = MyPhone()
phone.call_by_4g()
phone.call_by_5g()
phone.read_card()
phone.write_card()
phone.control()

# 同名成员属性或者方法，按继承优先级（左边）的来，即(Phone2022, NFCReader, RemoteControl)中Phone2022和NFCReader都有producer属性，调用时会选用Phone2022的
print(phone.producer)

