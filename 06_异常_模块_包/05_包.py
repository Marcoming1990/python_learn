"""
从物理上看，包就是一个文件夹，在该文件夹下包含了一个__init__.py文件，该文件夹可包含多个模块文件
从逻辑上看，包的本质依然是模块
"""
# 创建一个包
# 导入自定义的包中的模块，并使用
# import my_package.module1
# import my_package.module2
#
# my_package.module1.info_print1()
# my_package.module2.info_print2()

# from my_package import module1
# from my_package import module2
# module1.info_print1()
# module2.info_print2()

# from my_package.module1 import info_print1
# from my_package.module2 import info_print2
# info_print1()
# info_print2()


# 通过__all__变量，控制import *
from my_package import *

module1.info_print1()
# module2.info_print2()  # 报错，因为__init__配置的__all__没有model2
