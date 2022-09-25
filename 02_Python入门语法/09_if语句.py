# if语句
age = 30
if age >= 18:
    print("我已经成年了")

# if else语句
age = int(input("请输入你的年龄："))
if age >= 18:
    print("成年人可以上网！")
else:
    print("未成年人出去！")

# if elif else语句
age = int(input("请输入你的年龄："))
vip = int(input("你是VIP客户吗？1=是，0=不是："))
if age >= 18:
    print("成年人可以上网！")
elif vip == 1:
    print("VIP客户随便上网！", vip)
else:
    print("未成年非VIP客户出去！")
