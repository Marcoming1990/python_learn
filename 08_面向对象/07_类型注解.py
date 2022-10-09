""""
    python3.5时候引入了类型注解，以方便静态类型检查工具，IDE等第三方工具
    类型注解：在代码中涉及数据交互的地方，提供数据类型的注解（显式说明）
    主要功能：
        - 帮助第三方IDE工具（如Pycharm）对代码进行类型推断，协助做代码提示
        - 帮助开发者自身对变量进行类型注释
    支持：
        - 对变量的类型注解
        - 对函数（方法） 形参列表 和 返回值 的类型注解
    语法：
        变量:类型
    其他方式：
        在注释中表示  # type: int
    不会报错：
        var_1: int = "hello"
    形参注解：
        def 函数名(形参:类型, 形参:类型...):
    返回值注解：
        def 函数名(形参:类型, 形参:类型...) -> 返回值类型:
    Union(联合)类型注解：
        Union[类型,...,类型]
"""
import json
import random
from typing import List, Tuple, Dict, Union

# 基础数据类型注解
var_1: int = 18
var_2: str = "hello"
var_3: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()
# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"hello", 666}

# 容器类型详细注解
# 注释部分写法报错，但视频教程没报错，上网学习后改为下面方法（需要导入包），弹幕说3.9版本前会报错
# my_list: list[int] = [1, 2, 3]
# my_tuple: tuple[int, str, bool] = (1, "hello", True)
# my_dict: dict[str, int] = {"hello", 666}
my_list1: List[int] = [1, 2, 3]
my_tuple1: Tuple[int, str, bool] = (1, "hello", True)
my_dict1: Dict[str, int] = {"hello", 666}

# 在注释中进行类型注解
var_11 = random.randint(1, 10)  # type: int
var_12 = json.loads('{"name":"zhangsan"}')  # type: dict[str, str]


def func():
    return 10


# 返回值是int类型
var_13 = func()  # type: int


# 形参注解 def 函数名(形参:类型, 形参:类型...):
def add(x: int, y: int):
    return x + y


# add()  # ctrl + p弹出提示


# 返回值注解 def 函数名(形参:类型, 形参:类型...) -> 返回值类型:
def func1(data: list) -> list:
    return data


# func1()

# Union类型注解（必须先导包）
my_list2: List[Union[int, str]] = [1, 2, "hello", "world"]  # list列表里面既有int类型，也有str类型


def func2(data: Union[int, str]) -> Union[int, str]:
    pass


# func2()
