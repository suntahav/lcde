# Write your MySQL query statement below
select name as Employee from Employee As e1 where (salary > (select salary from Employee where id = e1.managerId))