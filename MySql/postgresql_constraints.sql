

create table stu
(sno int primary key,sname varchar(50) unique,
 marks float check(marks>35),is_active boolean default 'true')
 
 alter table stu add column course varchar(50) not null default('MPC')
 
 insert into stu values(101, 'hussain', 36)
insert into stu values(102, 'valli', 37)
insert into stu values(105, 'valli', 33)

-- To remove checked constriant 
alter table stu drop constraint stu_marks_check

-- TO remove unique key constraint
ALTER TABLE stu DROP CONSTRAINT stu_tname_key
alter table stu drop index test -- in sql 

-- TO remove primary key constraint
ALTER TABLE stu DROP CONSTRAINT stu_pkey

-- drop defaut constraint--
alter table emp alter column is_active drop default
--

-- To drop not null constraint 
alter table stu alter column course drop not null

-- TO add primary key constraint and unique key
ALTER TABLE stu add primary key(sno)
alter table s2 add unique(sname)

-- TO add foreign key constraint
ALTER TABLE stu add foreign key(child_col_name) references parent_table_name(parent_col_name)

-- To add not null constraint
alter table stu alter column is_active set not null

-- To add default  constraint
alter table s2 alter column is_active set default('true')

-- To add checked constraint
alter table s2 add check(marks>35)
