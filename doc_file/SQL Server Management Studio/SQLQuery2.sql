create table emp
(empid int not null,
firstname varchar(20) not null,
midname varchar(20) null,
lastname varchar(20) not null,
govtid char(10) null,
dob date not null )

-- adding additional columns
alter table emp
add dept varchar(10)

select * from emp
-- deleting column & altering it

alter table emp
drop column dept

alter table emp
add dept varchar(15)

-- altering table directly
alter table emp
alter column dept varchar(20)

insert into emp values(132,'Dylan','A','Word','HN513777D','19920914','Customer Relations')
--or
insert into emp([firstname],[midname],[lastname],[govtid],[dob],[dept],[empid])
values('Joseph','H','Wright','TX593671R','19711224','Litigation',131)

select * from emp order by empid
-- inserting into table from excel
-- copy all data -> right click on table -> edit top 200 rows -> paste

create table emp1 
(empid int not null,
empname varchar(50) not null,
deptd int null,
salary int null,
managerid int null,
age int null)

alter table emp1
add dob date

select * from emp1
select * from emp1 where empname like 'A%'

--% -> 0-infinity characters
--_ -> 1 character
--[A-G] -> in range A-G
--[AGQ] -> A,G or Q
--[^AGQ] -> not A,G or Q
select * from emp1 
where empname like '[r-t]%'

select * from emp1 
where empname like '[^rst]%'


select * from emp1 
where empname like '[%]%'  -- it shows name starts with % has any character afterwards

select year(dob)
from emp1;


select year(dob),count(*)
from emp1
group by year(dob)
order by year(dob) desc

select top(5) * from emp1 -- it is like limit in mysql

select  top(5) left(empname,1) as letter,count(*) count
from emp1
group by left(empname,1)
order by count(*) desc


select left(empname,1) as letter,count(*) count
from emp1
group by left(empname,1)
having count(*)>1
order by count(*) desc

select DATEPART(month,dob),count(*) --datepart gives month number etc
from emp1
group by DATEPART(month,dob)


select DATEname(month,dob),count(*) --it gives month name
from emp1
group by DATENAME(month,dob)
order by DATENAME(month,dob) -- but this will not order correctly as ordering done in alphabetical order therefore next query


select DATENAME(month,dob),count(*) --datepart gives month number etc
from emp1
group by DATENAME(month,dob), DATEPART(month,dob) --since we are using datepart in orderby hence used here also
ORDER by DATEPART(month,dob)
-- if we have to group by something & order by something else we have to use both column in group by clause


select DATENAME(month,dob),count(*),year(dob)
from emp1
group by DATENAME(month,dob),year(dob)
order by YEAR(dob)

-------------------------------File 11--------------------------------
-- adding a table
select * from Transaction_tbl --emp1

create table Transaction_tbl(
Amount smallmoney not null,
Date_of_transaction smalldatetime null,
empid int not null) --where empiid is a foreign key from emp1

select e.empid,empname,amount
from emp1 as e
join Transaction_tbl as t
on e.empid=t.empid

select e.empid,empname,sum(amount)--need to group every other statement except summerising statement(sum,count,avg etc)
from emp1 as e
join Transaction_tbl as t -- left join, right join, cross join
on e.empid=t.empid
group by e.empid,empname
order by e.empid

-- derived table
select count(deptd) as totaldepts
from
(select deptd,count(*) as numberofemployee
from emp1
group by deptd) as newtable
-- or
select count(distinct deptd) from emp1

-- creating a table based on results of select statements
select distinct deptd,'' as dept_head -- it creates a column with varchar(1) type with no data in that col
into dept_tbl						  -- also N'' creates column with nvarchar(1) type
from emp1

drop table [dbo].[dept_tbl]
-- creating the above same table with varchar(20)
select distinct deptd, CONVERT(varchar(20),'') as dept_head
into dept_tbl
from emp1
-- or
alter table dept_tbl
alter column dept_head varchar(30) null

-- joining 3 tables emp1,transaction_tbl,dept_tbl
select * 
from dept_tbl as d
join emp1 as e
on d.deptd=e.deptd -- matching row is deptd
join Transaction_tbl as t
on e.empid=t.empid  -- matching row is empid

--go
select d.deptd,dept_head,sum(amount)
from dept_tbl as d
left join emp1 as e
on d.deptd=e.deptd -- matching row is deptd
left join Transaction_tbl as t
on e.empid=t.empid  -- matching row is empid
group by d.deptd, d.dept_head

----------------------------------------File 12-------------------------------------------
-- Missing Data
select e.empid as Enumber,t.empid as Tnumber,empname,sum(amount) as total_amount
from emp1 as e
join Transaction_tbl as t
on e.empid=t.empid
group by e.empid,t.empid,empname

-- doing same query using left join
select e.empid as Enumber,t.empid as Tnumber,empname,sum(amount) as total_amount
from emp1 as e
left join Transaction_tbl as t
on e.empid=t.empid
group by e.empid,t.empid,empname
-- Here the rows in Tnumber column has null values which means, The rows which has null values are the
-- employees who didnt make any transactions
go
-- Now query to find the names of emps who didnt make ny transactions
select empname,Enumber from 
(select e.empid as Enumber,t.empid as Tnumber,empname,sum(amount) as total_amount
from emp1 as e
left join Transaction_tbl as t
on e.empid=t.empid
group by e.empid,t.empid,empname) as new_table
where Tnumber is null
order by Enumber



-- right join
select e.empid as Enumber,empname,t.empid as Tnumber,sum(amount) as total_amount
from emp1 as e
right join Transaction_tbl as t
on e.empid=t.empid
--where e.empid is null
group by e.empid,t.empid,empname
-- Now if any row of Enumber column is null, then that means there is a person who have done some 
-- transactions But dont have any empid i.e they are not the employees of the organisation
-- we have a query below to delete those transaction data

------------ Deleting data
-- begin transaction& rollback transaction is used to undo the query done
begin transaction

delete Transaction_tbl
--select *
from emp1 as e					--here emp1 id is used to create join not to delete from it & Also
right join Transaction_tbl as t --table used in from clauseis for checkig where statement, not for deleting
on e.empid=t.empid
where e.empid is null

select * from Transaction_tbl
rollback transaction

-- or
begin transaction

delete Transaction_tbl
from Transaction_tbl
where empid in (select tnumber
from
(select e.empid as enumber ,t.empid as tnumber
from emp1 as e
right join Transaction_tbl as t
on e.empid=t.empid) as new_table
where enumber is null)

select * from Transaction_tbl
rollback transaction

---- updating all the the transactions of empid 3 as of empid 18 
select * from Transaction_tbl;
begin transaction

update Transaction_tbl
set empid=18
output inserted.* , deleted.* --It is an optional line which display new/old result(table) based on command used
--output deleted.*  -- it gives deleted rows
from Transaction_tbl
where empid=3
-- where empid between 3 and 10
-- where empid in(4,5,6)
select * from Transaction_tbl
rollback transaction
----------------------------------------------------------------------------------------------------
create table Transac_tbl2(
Amount smallmoney not null,
Date_of_transaction smalldatetime null,
empid int null)
-- To insert values of 1 table into already created table
insert into Transac_tbl2(Amount,Date_of_transaction,empid)
select *  from  Transaction_tbl

-- To insert values of 1 table into another table while creating it
--select * 
--into table_name
--from Transaction_tbl
