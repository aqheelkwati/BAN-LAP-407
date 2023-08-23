 -- view ->object explorer f8
 -- view -> properties f4
 -- tools-->options->all languages--> line mark
 ----------------------- To edit a table structure------------------------
 --right click on table-> script table as -> create to -> new query editor window
 
 -- adding rows using GUI
 -- right click on table--> edit top 200 rows --> edit rows & close

 
-- for refreshing cache
-- edit --> intelliscence --> refresh local cache

-- datatypes

--different types of int
-- 1)big int, int(upto 2 million), smallint(-32767->32768), tinyint(0-255)



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