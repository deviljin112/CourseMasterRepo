use Northwind;

select
    count(*) as 'Quantity of Discontinued Products'
from Products
where Discontinued = 1