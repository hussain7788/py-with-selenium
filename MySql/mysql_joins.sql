select * from s2

-- Inner join
select d.dname, count(s.sname) as "students"
from s2 s inner join dept d
on s.dno=d.dno
group by d.dname
having d.dname='CSE' or count(s.sname)>2

select * from dept

-- full join
select * 
from s2 s full join dept d
on s.dno=d.dno

-- Self join
select *
from s2 t1, s2 t2
where t1.sname= t2.sname

-- cross join

select * from s2, dept