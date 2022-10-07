# json就是不同编程语言之间、通用的数据交流格式（就像全球通用语言英语）
# json本质就是字符串，数据像Python的字典或包含多个字典元素的列表

import json

# 准备列表，列表内每个元素都是字典，将其转换为JSON
data = [{"name": "小明", "age": 11}, {"name": "小红", "age": 12}, {"name": "小王", "age": 13}]
json_str = json.dumps(data, ensure_ascii=False)  # ensure_ascii=False 可以显示中文
print(type(json_str))  # json - 特定格式的字符串
print(json_str)  # '[{"name": "小明", "age": 11}, {"name": "小红", "age": 12}, {"name": "小王", "age": 13}]'

# 准备字典，将字典转为JSON
d = {"name": "张三", "addr": "广州"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将JSON字符串转为Python数据类型[{k:v,k:v},{k:v,k:v}]
s = '[{"name": "小明", "age": 11}, {"name": "小红", "age": 12}, {"name": "小王", "age": 13}]'
l = json.loads(s)
print(type(l))  # 转回Python的列表list
print(l)

# 将JSON字符串转为Python数据类型{k:v,k:v}
s = '{"name": "张三", "addr": "广州"}'
d = json.loads(s)
print(type(d))  # 转回Python的字典dict
print(d)
