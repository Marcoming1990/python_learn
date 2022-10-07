from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()
# 准备数据
data = [
    ("山东", 9),
    ("黑龙江", 19),
    ("湖南", 199),
    ("台湾", 599),
    ("四川", 1099),
    ("新疆", 10099),
]
# 添加数据
map.add("测试地图", data, "china")
# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 显示地图颜色
        is_piecewise=True,  # 开启手动校准
        pieces=[  # 校准范围
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "100-499", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "500-999", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#CC3333"},
            {"min": 10000, "label": "10000以上", "color": "#990033"},
        ]
    )
)

# 绘图
map.render()
