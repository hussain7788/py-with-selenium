create database group_order;
use group_order;

create table emp(eno int primary key not null auto_increment, ename varchar(30), sal decimal, age int, gender varchar(10));
insert into emp values(1,"anil", 20000, 24, "male", "hyd", "ece"),(2,"sunil", 30000, 24, "male", "hyd", "ece"),(3,"ajay", 25000, 25, "male", "chennai", "cse"),
(4,"pinky", 30000, 24, "female", "chennai", "cse"),(5,"swati", 35000, 26, "female", "bang", "ece");
delete from emp where eno=100;
alter table emp add column dname varchar(50);

select * from emp;

Q)write a query to display no of emps working in each dept 

----- grouping department names in single column and getting working employees in dept -----
select dname, count(ename) as "no of emps" from emp group by dname;
----- end -----
Q) query to display sum of salary of each department 
select dname,sum(sal) as "total salary" from emp group by dname;

Q) query to display no of males and females working in company
select gender, count(gender)as "no_emps" from emp group by gender;

Q) query to display no of emps working in each city
select city,count(city) as "no_emps" from emp group by city;

Q) query to display sum salary of each dept based on having class condition;
select dname, count(ename), sum(sal) as "total sal" from emp group by dname having sum(sal)>55000;

Q) query to display total employees in each city based on having clause condition;
select city, count(city) from emp group by city having count(city)>=2;

Q)second maximum salary from emp
select * from (select * from emp order by sal desc limit 2)E order by sal asc limit 1

Q) query to find 3rd maximum salary from emp
select max(sal) from emp where sal<(select max(sal) from emp where sal<(select max(sal) from emp));



----- triggers ----

use group_order

delimiter //
create trigger m2
before update 
on emp
for each row begin
insert into stu
set sno = old.eno,
sname = old.ename;
end //
update emp set ename="sudha" where eno=5;

DROP trigger m2;

update emp set ename="sudha" where eno=5;

-------- end -----------

use group_order
delimiter //
create trigger m2
before update 
on emp
for each row begin
insert into stu
set sno = old.eno,
sname = old.ename;
end //
DROP trigger m2;

update emp set ename="sudha" where eno=5;
