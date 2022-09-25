# while循环
def list_while_func():
    mylist = ["wow", "pretty", "python"]
    index = 0
    while index < len(mylist):
        element = mylist[index]
        print(f"列表元素：{element}")
        index += 1


list_while_func()


# for循环
def list_for_func():
    mylist = [1, 2, 3, 4, 5]
    for element in mylist:
        print(f"列表元素：{element}")


list_for_func()
