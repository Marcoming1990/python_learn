# continue循环跳过
for i in range(1, 6):
    print("语句1")
    continue  # 循环临时中断，跳过语句2，进入下一个循环
    print("语句2")

# continue嵌套应用
for i in range(1, 3):
    print("漂亮1")
    for j in range(1, 4):
        print("漂亮2")
        continue  # 循环临时中断，跳过漂亮3，进入下一个循环
        print("漂亮3")
    print("漂亮4")
