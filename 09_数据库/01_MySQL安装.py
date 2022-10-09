"""
    免费版本：MySQL Community Server
    下载地址：www.mysql.com
            http://downloads.mysql.com/archives/installer
            mysql install for windows
    安装程序（全默认-输密码-尝试连通）：
            1、developer default -next
            2、next - yes
            3、Execute - next
            4、next - development Computer - next - next
            5、设置root管理员密码 - next
            6、后面默认next和finish，会让你输一次密码链接数据库
    简单配置：
            我的电脑-右键属性-高级系统设置-环境变量-path-新建-复制路径：C:\Program Files\MySQL\MySQL Server 5.7\bin
    验证配置：
            进入cmd，输入：mysql -uroot -p
            输入密码，此处是：lzq
            成功：Welcome...
    常用操作：
            cmd进入mysql>之后
            1、show databases;   查看有哪些数据库
            2、use 数据库名;       使用某个数据库
            3、show tables       查看数据库内有哪些表
            4、exit              退出MySQL的命令行环境
            
    可视化软件DBeaver：
            跨平台、开源、免费的图形化工具
            下载网址：dbeaver.io
            下载版本：DBeaver Community（免费）
                    Windows(installer)
            安装程序：默认安装（路径可以改）
            打开软件：
                    1、否，不用创建数据库
                    2、选择MYSQL，填写密码
                    3、测试链接，下载，已连接，确定
"""

