use joins
select * from emp

delimiter //
create procedure proc_add_emp(tablename varchar(30), eno int, ename varchar(30), sal decimal)
begin
insert into emp values(eno, ename, null, 30000);
end //
call proc_add_emp("emp", 7, "kanna", 20000)

delimiter //
create procedure max_sal()
begin
select * from emp order by sal desc;
select "mynameis";
end //
call max_sal

delimiter //
create procedure max_sal_third()
begin
select * from (select * from emp order by sal desc limit 3)E order by sal asc limit 1;
end //
call max_sal_third;
