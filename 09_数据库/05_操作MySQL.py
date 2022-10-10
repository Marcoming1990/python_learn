# pip install pymysql （因为本地有python2和3版本，所以cmd输入pip3 install pymysql）
# 安装的第三方包目录：D:\studio\Python\software\Python 3.8.3\Lib\site-packages

from pymysql import Connection

# 获取到MySQL数据库的链接对象
conn = Connection(
    host="localhost",  # 主机名（IP）
    port=3306,  # 端口
    user="root",  # 账户
    passwd="laizhiqiang",  # 密码
    # autocommit=True  # 设置自动提交，那insert时候不用手动commit()
)

print(conn.get_server_info())  # 打印数据库信息(5.7.12-log) 表示链接成功

# 选择数据库 - 创建表
cursor = conn.cursor()  # 获取游标对象
conn.select_db("test")  # 选择数据库
# cursor.execute("create table test_pymysql(id int);")  # 执行sql，这里代码中可以不写;

# 执行插入SQL
# cursor.execute("insert into student value(1002,'王多',20)")
# conn.commit()  # 通过commit确认，不然不会生效到数据库

# 执行删除SQL
# cursor.execute("delete from student where id = 1")
# conn.commit()

# 执行修改SQL
# cursor.execute("update student set name = \'好多鱼\' where id = 1001")
# conn.commit()

# 执行查询SQL
cursor.execute("select * from student")
results = cursor.fetchall()
# print(results)  # ((1, '周杰伦', 31), (2, '林俊杰', 35))
for r in results:
    print(r)

# 关闭链接
conn.close()
