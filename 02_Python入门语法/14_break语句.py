# break循环中断
for i in range(1, 101):
    print("语句1")
    break
    print("语句2")
print("语句3")

# break嵌套应用
for i in range(1, 3):
    print("漂亮1")
    for j in range(1, 6):
        print("漂亮2")
        break
        print("漂亮3")
    print("漂亮4")
