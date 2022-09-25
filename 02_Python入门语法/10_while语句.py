import random

# while语句
i = 1
while i <= 100:
    print(f"表白100次，现在是第{i}次")
    i += 1

# 案例：猜范围1-100的随机数字
num = random.randint(1, 100)
# 定义一个变量去记录猜测次数
count = 0
# 通过一个布尔类型的变了，做循环是否继续的标记
flag = True
while flag:
    guess_num = int(input("请输入你猜测的数字："))
    count += 1
    if guess_num == num:
        print("恭喜你，猜对了！")
        flag = False
    else:
        if guess_num > num:
            print("你猜大了")
        else:
            print("你猜小了")
print(f"你一共猜了{count}次")
