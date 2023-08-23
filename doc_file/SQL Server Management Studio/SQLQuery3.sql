----------------------------------SESSION 3-------------------------------------------
--Different constraints

-- adding constraints to a table
select * from emp1;

alter table emp1
add constraint uniqueempid unique(empid); --uniqueempid is constraint name(can be anything)
-- if there are already some duplicate rows present then the above query will throw error 
-- so we have to delete duplicate rows.

select empid,count(empid) as mycount
from emp1
group by empid
having count(empid)>1;