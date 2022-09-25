"""
字符串的三种定义方式
- 单引号定义法
- 双引号定义法
- 三引号定义法
"""
# 单引号定义法
name = '单引号'
print(type(name))
# 双引号定义法
name = "双引号"
print(type(name))
# 三引号定义法
name = """
我是
三引号
"""
print(type(name))


# 在字符串内 包含双引号
name = '"小明"'
print(name)
# 在字符串内 包含单引号
name = "'小红'"
print(name)
# 使用转义字符\ 解除引号的效果
name = "\"小白\""
print(name)
name = '\'小黑\''
print(name)