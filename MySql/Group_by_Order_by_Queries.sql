create database group_order;
use group_order;

create table emp(eno int primary key not null auto_increment, ename varchar(30), sal decimal, age int, gender varchar(10));
insert into emp values(1,'anil', 20000, 24, 'male', 'hyd', 'ece'),(2,'sunil', 30000, 24, 'male', 'hyd', 'ece'),(3,'ajay', 25000, 25, 'male', 'chennai', 'cse'),
(4,'pinky', 30000, 24, 'female', 'chennai', 'cse'),(5,'swati', 35000, 26, 'female', 'bang', 'ece');
delete from emp where eno=100;
alter table emp add column dname varchar(50);

select * from emp;

Q)write a query to display no of emps working in each dept 

----- grouping department names in single column and getting working employees in dept -----
select dname, count(ename) as 'no of emps' from emp group by dname;
----- end -----
Q) query to display sum of salary of each department 
select dname,sum(sal) as 'total salary' from emp group by dname;

Q) query to display no of males and females working in company
select gender, count(gender)as 'no_emps' from emp group by gender;

Q) query to display no of emps working in each city
select city,count(ename) as 'no_emps' from emp group by city;

Q) query to display sum salary of each dept based on having class condition;
select dname, count(ename), sum(sal) as 'total sal' from emp group by dname having sum(sal)>55000;

Q) query to display total employees in each city based on having clause condition;
select city, count(city) from emp group by city having count(city)>=2;

Q)second maximum salary from emp
select * from (select * from emp order by sal desc limit 2)E order by sal asc limit 1

Q) query to find 3rd maximum salary from emp
select max(sal) from emp where sal<(select max(sal) from emp where sal<(select max(sal) from emp));
select * from (
select distinct marks from stu order by marks limit 3)E order by marks desc limit 1

select sal from(
select sal from emp order by sal desc limit 3)E order by sal asc limit 1;

----- CTE common table expression------
----- using partition by order by-------

Q) query to group common values in column in partition
    select *, row_number() over(partition by pname order by pname) as "rid" from person

Q)Query to get >1 records means duplicate records
    select * from (
        select *, row_number() over(partition by pname order by pname) as "rid" from person)E where rid>1

Q) Query to delete duplicate records from table using CTE 
    ---------very important query to delete duplicate records-----
    WITH cte_rental AS (
	    select *,row_number() over(partition by pno order by pno) as "rid" from person
    )
        delete from cte_rental where rid>1

-----end of CTE by partition -----------------

----- using ranking functions ---------------

select *, row_number() over(order by marks) as 'rid',
		rank() over(order by marks) as 'rank id',
        dense_rank() over(order by marks) as 'den id',
        row_number() over(partition by marks order by marks) as 'par id'
        from stu
        id, name, marks, doj,       rid, rank, den, parti
        1	valli	40	2024-01-22	1	    1	1	1
        2	hussain	40	2024-01-21	2	    1	1	2
        5	kanna	50	2024-01-20	3	    3	2	1
        6	chinna	50	2024-01-17	4	    3	2	2
        4	sunil	60	2024-01-19	5	    5	3	1
        3	anil	90	2024-01-18	6	    6	4	1
------ end -------------------------

------- inner join and group by under public schema django models---------


SELECT * FROM public."SignalsApp_company"
ORDER BY id ASC LIMIT 100

select * from public."SignalsApp_language"
order by id asc limit 100

select * from public."SignalsApp_programmer"
order by id asc limit 100

select * from public."SignalsApp_programmer_language"
order by id asc limit 100

select c.name, count(p.name)
from public."SignalsApp_company" as c inner join public."SignalsApp_programmer" as p
on c.id = p.company_id group by c.name

select l.name, count(p_l.programmer_id)
from public."SignalsApp_programmer_language" as p_l inner join public."SignalsApp_language" as l
on p_l.programmer_id = l.id
group by l.name

-----------end ------------------------------

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
update emp set ename='sudha' where eno=5;

DROP trigger m2;

update emp set ename='sudha' where eno=5;

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

update emp set ename='sudha' where eno=5;
