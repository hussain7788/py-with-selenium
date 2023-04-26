select * from dept

select * from emp

update emp set dno=2 where eno=5

select emp.eno,emp.ename,emp.sal,emp.age,dept.dname from dept inner join emp on dept.dno=emp.dno

select emp.eno,emp.ename,emp.sal,emp.age,dept.dname from dept inner join emp on dept.dno=emp.dno where emp.sal between 20000 and 30000 and dept.dname='ece'

select emp.eno,emp.ename,emp.age,dept.dname from dept inner join emp on dept.dno=emp.dno where emp.age between 20 and 25

select e.eno,e.ename,e.age,d.dname from dept d inner join emp e on d.dno=e.dno where e.age between 20 and 25

select ename from emp where ename like 'a%'

create table ins(ino int, eno int)

insert into ins values(1, 1),()
drop table ins
-- full join--
select emp.*, dept.* from dept full join emp on dept.dno=emp.dno
-- full join except matching records--
select emp.*, dept.*, from dept full join emp on dept.dno=emp.dno where dept.dno is null and emp.dno is null
-- left join 
select emp.*, dept.* from emp left join dept on emp.dno=dept.dno
--only left records--
select emp.*, dept.* from emp left join dept on emp.dno=dept.dno where dept.dno is null
-- only right records--
select emp.*,dept.* from emp right join dept on emp.dno=dept.dno where emp.dno is null
--equi join use , in inner join and where on condition --
select emp.eno,emp.ename,emp.sal,emp.age,dept.dname from dept,emp where dept.dno=emp.dno
-- non equi join except = use any operator--
select emp.*,dept.* from emp,dept where emp.dno between 1 and 2

alter table emp drop dept

insert into dept values(4, 'eee')

select * from emp,dept

------------------------
country, city, country language table joins
------------------------------

--- join country and city and fetching number of cities in each country by group by
--- in the result filtering the countries who having more than 300 cities in each country
select c1.code, c1.population, count(c2.countrycode_id) as "total cities"
from app1_country c1 inner join app1_city c2
on c1.code = c2.countrycode_id
group by c1.code
having count(c2.countrycode_id)>300

--- join country and countrylanguage and fetching number of countrylanguages in each country by group by
--- in the result filtering the countries of india

select c1.code,c1.name, count(c2.language) as "total languages"
from app1_country c1 inner join app1_countrylanguage c2
on c1.code = c2.countrycode_id
group by c1.code
having c1.name='India'

--- join country and city and country language and fetching entire data
--- in the result filtering the countries of india and city of hyderabad

select c1.code,c1.name, c2.name as "city name", c2.countrycode_id, c3.language as "country language", c3.countrycode_id
from app1_country c1 inner join app1_city c2
on c1.code = c2.countrycode_id
inner join app1_countrylanguage c3
on c2.countrycode_id = c3.countrycode_id
where c1.name = 'India' and c2.name = 'Hyderabad'