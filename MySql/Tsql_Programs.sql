create database tsql
use tsql
create table emp(eno int, ename varchar(30), sal decimal , age int)
insert into emp values(101, "hussain", 30000, 23),(102, "valli", 40000, 24),(103, "ramu", 50000, 25)

select * from emp

declare 
@eno int, @ename varchar(30), @sal decimal, @age int
begin
set @eno = 101
set @ename =(select ename from emp where eno=@eno)
set @sal =(select sal from emp where eno=@eno)
set @age =(select age from emp where eno=@eno)
end

declare 
@fullname varchar(30)
begin
set @fullname="hussain"
print @fullname
end

