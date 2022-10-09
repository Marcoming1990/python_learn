"""
    SQL：结构化查询语言，用于访问和处理数据库的标准的计算机语言
    经过多年发展，SQL已成为数据库领域统一的数据操作标准语言，可以说几乎市面上所有的数据库系统都支持使用SQL语言来操作
    简而言之，SQL语言是操作数据库的专用工具
    SQL语言的分类：
        1、数据定义：DDL
            库的创建删除、表的创建删除等
        2、数据操纵：DML
            新增数据、删除数据、修改数据等
        3、数据控制：DCL
            新增用户、删除用户、密码修改、权限管理等
        4、数据查询：DQL
            基于需求查询和计算数据
    SQL语法特征：
        1、大小写不敏感（show databases; = SHOW DataBases;）
        2、可以单行或多行书写，最后以;号结束
        3、SQL支持注释：
            - 单行注释：-- 注释内容（--后面一定要有一个空格）
            - 单行注释：# 注释内容（#后面可以不加空格，推荐加上）
            - 多行注释：/* 注释内容 */
    DDL - 库管理：
        1、show databases;       查看数据库
        2、use 数据库名称;        使用数据库
        3、create database 数据库名称 [charset utf8];     创建数据库
            create database xx; 或 create database xx charset utf8;
        4、drop database 数据库名称;      删除数据库
        5、select database();    查看当前使用的数据库
    DDL - 表管理：
        1、show tables;      查看有哪些表
        2、create table student(       创建表
                id int,
                name varchar(10),
                age int
           );
           列类型有：
                1）int - 整数
                2）float - 浮点型
                3）varchar(长度) - 文本，长度为数字，最大长度255
                4）date - 日期类型
                5）timestamp - 时间戳类型
        3、drop table 表名称;   删除表
           drop table if exists 表名称;
"""