# Echarts是百度开源的数据可视化，结合Python=pyecharts
# 官网 pyecharts.org
# gallery.pyecharts.org 预览效果图的网站

# 导包（折线图案例）
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折线图对象
line = Line()
# 给折线图对象添加x轴的数据
line.add_xaxis(["中国", "美国", "英国"])
# 给折线图对象添加Y轴的数据
line.add_yaxis("GDP", [30, 20, 10])

# 设置全局配置项（所有图例通用设置：标题、图例、工具箱等）
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),  # 标题
    legend_opts=LegendOpts(is_show=True),  # 图例
    toolbox_opts=ToolboxOpts(is_show=True),  # 工具箱
    visualmap_opts=VisualMapOpts(is_show=True),  # 视觉映射
)

# 通过render方法，将代码生成为图像
line.render()  # 生成一个render.html在目录下，用浏览器打开
