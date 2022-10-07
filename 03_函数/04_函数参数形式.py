"""
演示多种传参的形式
"""


def user_info(name, age, gender):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")


# 位置参数 - 默认使用形式（对应参数顺序）
user_info("小明", 22, "男")

# 关键字参数
user_info(name="小红", age=11, gender="女")
user_info(age=10, gender="女", name="大红")  # 关键词参数可以不按顺序
user_info("老王", gender="男", age=40)  # 默认参数要放前面


# 缺省参数（默认参数）
def user_info(name, age, gender="男"):  # 默认性别是男，且位置必须放后面
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")


user_info("小肥", 30)
user_info("小肥", 30, gender="女")


# 不定长参数（可变参数）
# 1、*号 - 位置不定长（不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):  # args是默认规范，但是不是强制
    print(f"args参数的类型是：{type(args)},内容是：{args}")


user_info(1, 2, 3, "小明", "男")


# 2、**号 - 关键字不定长（key-word)
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)},内容是：{kwargs}")


user_info(name="小明", age=11, gender="男")
