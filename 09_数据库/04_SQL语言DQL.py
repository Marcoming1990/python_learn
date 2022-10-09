"""
1、基础数据查询
select id,name from student;  # 查询id和name列
select * from student;    # 查询所有列
select * from student where age > 20;    # 条件查询

2、分组聚合
select gender, avg(age) from student group by gender;  # 男女分组，求男女平均年纪，后面by有gender，前面select才能写gender
select gender, avg(age), sum(age), min(age), max(age), count(*) from student group by gender;   #  count(具体列)跟* 效果一样，男有多少人，女多少人

3、排序
select * from student where age > 20 order by age asc;   # 大于20岁的学生，根据年龄从小到大升序（asc），不写asc默认也是升序，如果降序是desc

4、分页
select * from student limit 5;  # 结果只取5条
select * from student limit 10, 5;  # 结果跳过前10条，从11条开始取5条

组合使用例子：
select age, count(*) from student where age > 20 group by age
order by age limit 3;  # 以大于20的年龄分组，每组有多少人，按升序只显示3条

"""