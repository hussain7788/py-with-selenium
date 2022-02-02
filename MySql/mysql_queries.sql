create database dj
use dj
create table emp(eno int , ename varchar(10), age int, m1 int, m2 int, m3 int)
select * from emp
insert into emp values(3, "ramu", 25, 70,70,90),(2, "valli", 24, 50,60,80)

alter table emp add m4 int
update emp set m4=68 where eno=1
alter table emp drop m4
truncate table emp
delete from emp where eno=3
drop table emp
select *, m1+m2+m3 as "Total" from emp
alter table emp drop m3
alter table emp add salary decimal
alter table emp rename column enames to ename
alter table emp modify column ename varchar(50)
desc emp
update emp set salary = 30000 where eno=3
update emp set salary = 40000 where eno=2

alter table emp rename column salary to sal

-- calculating da,hra,total salary --
select *, (0.3*sal) as "da", (0.2*sal) as "hra" ,sal+(0.3*sal)+(0.2*sal) as "total sal" from emp 
-- end -- 

select * from emp where age>25
drop table emp
create table emp(eno int AUTO_INCREMENT primary key, ename varchar(10), sal decimal, age tinyint)
insert into emp values(1,"hussain", 30000, 23),(2,"valli", 40000, 24), (3,"ramu", 50000, 25)
select * from emp where ename like "h%" 
select * from emp where ename like "%n"
select * from emp where ename like "h%" or ename like "%i"

-- second maximum salary from emp table -- 
select max(sal) from emp where sal<(select max(sal) from emp)
-- end --

desc emp
show tables
alter table emp modify column ename varchar(60) not null
-- constraints --
1. null constraint
2. not null constraint
3. primary key constraint
4. unique key constraint
5. check constraint
6. default constraint
7. foreign key constraint
-- end --
-- checked constraint will work based on condition
create table e1(eno int check(eno>100), ename varchar(10))
insert into e1 values(101, "hussain") #success
insert into e1 values(99, "hussain") #fail
alter table e1 add column salary decimal check(salary between 20000 and 30000)
update e1 set salary=25000 where eno=101 #success
update e1 set salary=10000 where eno=101 #fail
alter table e1 add column age tinyint check(age>=18 and age<=30)
update e1 set age=17 where eno =101 #fail
update e1 set age=18 where eno=101 # success
alter table e1 add column address varchar(40) default("A")
insert into e1 values(102, "valli", 25000, 20
desc e1











SET SQL_SAFE_UPDATES = 0;





