create database mydb;
use mydb;

create table emp_compensation (
emp_id int,
salary_component_type varchar(20),
val int
);
insert into emp_compensation
values (1,'salary',10000),(1,'bonus',5000),(1,'hike_percent',10)
, (2,'salary',15000),(2,'bonus',7000),(2,'hike_percent',8)
, (3,'salary',12000),(3,'bonus',6000),(3,'hike_percent',7);
select * from emp_compensation;

-- Pivoting table
select emp_id,
sum(case when salary_component_type='salary' then val end) as salary,
sum(case when salary_component_type='bonus' then val end) as bonus,
sum(case when salary_component_type='hike_percent' then val end) as hike_percent
into emp_compensation1
from emp_compensation
group by emp_id;

select * from emp_compensation1;
-- This wont give the expected output
/*
select emp_id, 'salary' as component_type, salary as val,
'bonus' as component_type, bonus as val,
'hike_percentage' as component_type, hike_percent as val
from emp_compensation1;
*/

-- unpivoting Table 
select *  into emp_compensation2 -- here after 'from' statement 'select & into' are executed So ordered data is not inserted into new_table
from (
select emp_id,'salary' as component_type,salary as val from emp_compensation1
union all
select emp_id,'bonus' as component_type,bonus as val from emp_compensation1
union all
select emp_id,'hike_percent' as component_type,hike_percent as val from emp_compensation1) a
order by emp_id;

select * from emp_compensation2;

------------------------------------------------------------------------
create table emp(
emp_id int,
emp_name varchar(20),
department_id int,
salary int,
manager_id int,
emp_age int);

insert into emp
values(1, 'Ankit', 100,10000, 4, 39);
insert into emp
values (2, 'Mohit', 100, 15000, 5, 48);
insert into emp
values (3, 'Vikas', 100, 10000,4,37);
insert into emp
values (4, 'Rohit', 100, 5000, 2, 16);
insert into emp
values (5, 'Mudit', 200, 12000, 6,55);
insert into emp
values (6, 'Agam', 200, 12000,2, 14);
insert into emp
values (7, 'Sanjay', 200, 9000, 2,13);
insert into emp
values (8, 'Ashish', 200,5000,2,12);
insert into emp
values (9, 'Mukesh',300,6000,6,51);
insert into emp
values (10, 'Rakesh',300,7000,6,50);
insert into emp values(1,'akash',300,8000,4,60);

select * from emp;

-- How to find duplicates in sql
select emp_id,count(emp_id) from emp group by emp_id having count(emp_id)>1;

-- How to delete Duplicate values
use mydb;
select *,count(emp_id) over (partition by emp_id) from emp;

with cte as (select *,ROW_NUMBER() over (partition by emp_id order by emp_id) as rn 
from emp)
delete from cte where rn>1;

select * from emp;

-- difference b/w union & union all
select * into emp1 from emp;

select manager_id from emp1
union all -- union removes duplicate values
select manager_id from emp;

-- Q4 difference b/w rank, row_number(), dense_rank()

-- Q5 employee who are not present in dept table
create table department(
 
 dept_id int,
 dept_name varchar(10)
 );
 
insert into department values(100,'Analytics');
insert into department values(300,'IT');

select * from department;

select * from emp where department_id not in (select dept_id from department);
-- or
select * from emp
left join department on emp.department_id=department.dept_id
where department.dept_id is null;

-- Q6 select 2nd highest salary in each department
select * from
(select emp.*, DENSE_RANK() over (partition by department_id order by salary desc) as rn from emp) a
where rn=2;

-- Q7 find all the transactions done by shilpa

create table orders(
 customer_name char(10),
 order_date date,
 order_amount int,
 customer_gender char(6)
 );
 
 insert into orders values('Shilpa','2020-01-01',10000,'Male');
 insert into orders values('Rahul','2020-01-02',12000,'Female');
 insert into orders values('Shilpa','2020-01-02',12000,'Male');
 insert into orders values('Rohit','2020-01-03',15000,'Female');
 insert into orders values('Shilpa','2020-01-03',14000,'Male');

select * from orders;

select * from orders where UPPER(customer_name)='SHILPA';

-- Q10 write a query to swap genders of customers
update orders 
set customer_gender=
case 
when customer_gender='Male' then 'Female'
when customer_gender='Female' then 'Male'
end;