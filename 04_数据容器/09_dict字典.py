# 定义字典
# 键值对的key和value可以是任意类型（key不可为字典）
# key不允许重复，重复添加等同于覆盖原有数据
# 没有下标索引，只能通过key值取得对应value
my_dict1 = {"小明": 99, "小红": 88, "小强": 77}
# 定义空字典
my_dict2 = {}  # 空集合只能set()
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1}，类型是：{type(my_dict1)}")
print(f"字典2的内容是：{my_dict2}，类型是：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3}，类型是：{type(my_dict3)}")
# 定义重复key的字典
my_dict1 = {"小明": 99, "小明": 88, "小强": 77}
print(f"重复key的字典的内容是：{my_dict1}")  # 新的会把老的覆盖掉
# 从字典中基于key获取value
my_dict1 = {"小明": 99, "小红": 88, "小强": 77}
score = my_dict1["小明"]
print(f"小明的考试分数是：{score}")
# 定义嵌套字典
stu_score_dict = {
    # "小明": {}, "小红": {}, "小强": {}
    "小明": {
        "语文": 98,
        "数学": 97,
        "英语": 96,
    }, "小红": {
        "语文": 88,
        "数学": 87,
        "英语": 86,
    }, "小强": {
        "语文": 78,
        "数学": 77,
        "英语": 76,
    }
}
print(f"学生的考试成绩是：{stu_score_dict}")
# 从嵌套字典中获取数据
# 看一下小强的语文成绩
score = stu_score_dict["小强"]["语文"]
print(f"小强的语文成绩是：{score}")

"""
字典的常用操作
"""
my_dict = {"小明": 99, "小红": 88, "小强": 77}
# 新增元素
my_dict["翠花"] = 66
print(f"新增元素之后：{my_dict}")
# 更新元素
my_dict["小明"] = 33
print(f"更新元素之后：{my_dict}")
# pop方法 - 删除元素
score = my_dict.pop("小明")
print(f"删除元素之后：{my_dict},小明的考试分数是：{score}")
# clear方法 - 清空元素
my_dict.clear()
print(f"清空元素之后：{my_dict}")
# keys方法 - 获取全部的key
my_dict = {"小明": 99, "小红": 88, "小强": 77}
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")
# 遍历字典
# 方式1：通过获取全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
print("---------------------------")
# 方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
# len方法 - 统计字典内的元素数量
num = len(my_dict)
print(f"字典中元素数量有：{num}个")


