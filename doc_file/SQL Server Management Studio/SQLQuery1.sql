 -- view ->object explorer f8
 -- view -> properties f4
 -- tools-->options->all languages--> line mark
 ------------------------------------starting with SQL--------------------------------------------------
 -- creating database
 create database xyz;

 -- new query
 select 1+1 result
 select 1*3 as result

 --------------------------------------Creating tables--------------------------------------------------
 -- creating table(using gui & query)
 use xyz;
 create table tbl2
 (mynumbers int)

 -- adding rows using query
 insert into tbl2
 values (234)

 insert into tbl2 
 values(678),(156),(478)

 -- creating a query to display
 select * from tbl2
 select * from tbl1

 -- deleting data(row)
 delete from tbl1 -- deletes everything from table(not table)
 -- or
 truncate table tbl2

 -- deleting table
 drop table tbl1

 -- creating an employee table
 use [70-461]
 
create table tblemployee
(empid int, empname varchar(30))

insert into tblemployee 
values(1,'John Smith')

 --------------------------------------Number types & Functions-------------------------------------------

-- declaring/initializing a variable
declare @myvar int=2
declare @mv smallint=5
-- changing variable (modyfying)
set @myvar=3
-- retrieving variable
set @myvar= @myvar*3
select @myvar as myVariable --op will be 9



-- non integer numbers
-- 2) decimal(M,D) m- maximum number D- decimals

declare @myvar as decimal(7,2)
-- or declare @myvar numeric(7,2)
set @myvar = 12345.67
select @myvar

-- 3) money & small money(takes only 4 decimal points)
declare @myvar smallmoney=1234.56789
select @myvar

-- 4) float(24)

-- Mathematical functions
declare @myvar numeric(7,2)=3
select power(@myvar,2)
select SQUARE(@myvar)
select SQRT(@myvar) 
go
declare @myvar numeric(7,2)=3.75
select FLOOR(@myvar) as myfloor -- it rounds 3.7 to 3
select ceiling(@myvar) as myceiling -- it rounds 3.7 to 4
select round(@myvar,0) as myround --it goes to nearest round i.e 4
select round(@myvar,1) as myround --it rounds it to 1 decimal place,gives 3.80
go
select pi() as mypi
select exp(1) as e
go
select ABS(-120) -- removes negative
select sign(-120) --gives -1
select sign(120) --gives 1
go
select rand(450)  -- it gives random value

-- converting 1 type of number into another
-- 1)implicit way
declare @myvar decimal(5,2)=3
select @myvar
-- 2)explicit way (casting)
select CONVERT(decimal(5,2),3)
select CAST(3 as decimal(5,2)) -- it is same as above

select CONVERT(decimal(5,2),1000) -- it shows error as 999.99 s biggest number with that type
select try_CONVERT(decimal(5,2),1000) -- it shows null if there is an error
select TRY_CAST(1000 as decimal(5,2))

 ----------------------------------String Data types & Functions-------------------------------------------
 -- 1)char - ASCII range -> takes 1 byte
 -- 2)varchar - ASCII range -> takes 1 byte  
 -- 3)nchar - UNICODE range -> takes 2 byte
 -- 4)nvarchar - UNICODE range -> takes 2 byte
 -- ASCII Is for english & european but when it goes out of range of ascii value we should use unicode

 declare @mychar as char(10)
 set @mychar='hello'
 select @mychar,len(@mychar) as length, DATALENGTH(@mychar) as datalength --op 5,10
 --datalength gives total length given while declaring
 go
 declare @mychar as varchar(10)
 set @mychar='hello'
 select @mychar,len(@mychar) as length, DATALENGTH(@mychar) as datalength --op 5,5
 go
 declare @mychar as nchar(10)
 set @mychar=N'heloڳ'
 select @mychar,len(@mychar) as length, DATALENGTH(@mychar) as datalength --op 5,20 as it takes 2 bytes 2*10
 go
 declare @mychar as nvarchar(10)
 set @mychar=N'heloڳ'
 select @mychar,len(@mychar) as length, DATALENGTH(@mychar) as datalength --op 5,10

 ------ string functions
 declare @myascii as varchar(10)=' hello '
 declare @myunicode as nvarchar(10)=N'heloڳ'

 select left(@myascii,2),right(@myunicode,2)
 select SUBSTRING(@myascii,3,2) -- start from 3rd letter(not index) print 2 letters
 select LTRIM(@myascii) as ltrim --removes spaces in the begining
 select RTRIM(@myascii)	--removes spaces in the end
 select LTRIM(RTRIM(@myascii)) -- removes spaces in both start & end
 select REPLACE(@myascii,'l','L')
 select upper(@myascii)
 select lower(@myascii)

-- joining 2 strings
declare @first nvarchar(20)='john'
declare @mid nvarchar(20)
declare @last nvarchar(20)='smith'

--select @first+@mid+@last -- ans will be null as @mid is null

-- select @first + iif(@mid is null,'',@mid) + @last 
-- or
-- select @first + case when @mid is null then '' else @mid end + @last
-- or
--select @first + coalesce(@mid,'') + @last  -- it takes mid if it isnt null else ''
-- or
select CONCAT(@first,' ',@mid,' ',@last)

--------------joining strings to number
select 'my salary is $'+ CONVERT(varchar(20),4567.7) -- the op is 4567.7 not 4567.70

select 'my salary is '+ FORMAT(4567.7,'C')
select 'my salary is '+ FORMAT(4567.7,'C','en-GB') -- c means currency , en-GB means euro 
select 'my salary is '+ FORMAT(4567.7,'C','fr-FR') -- To search more 'standart numeric format strings'


 ----------------------------------Date data type-------------------------------------------
 declare @date datetime2 ='2015-01-01 03:04:05' --datetime also works
 --declare @date datetime2 ='20150101 03:04:05'
 select @date

 -- current date
 select CURRENT_TIMESTAMP
 select GETDATE()
 select SYSDATETIME()
 -----
select DATEADD(YEAR,1,'2015-01-01 03:04:05') --adds year/month/day etc to given date
select DATEpart(hour,'2015-01-01 03:04:05') as hour --parts year/month/day etc to given date
select DATENAME(WEEKDAY,'2015-01-01 03:04:05')
-- datediff