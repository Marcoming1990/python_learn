"""
create table student(
    id int,
    name varchar(10),
    age int
);

1、insert 数据插入
insert into student(id) values(1),(2),(3);  # 一次插入3条数据id=1、id=2、id=3
insert into student(id, name, age) values(4, '周杰伦', 31),(5, '林俊杰', 35);  # sql只支持单引号'
insert into student values(6, '张三', 31),(7, '李四', 35); # 位置要跟表头11对应

2、delete 数据删除
delete from student where id = 1;   # 删除id=1的数据，操作符包括：=、<、>、<=、>=、!=等等
delete from student;  # 没有where条件，会将所有数据清空

3、update 数据更新
update student set name = '王五' where id = 4;
update student set name = '老六' ;       # 没有where条件，列所有数据会修改

"""