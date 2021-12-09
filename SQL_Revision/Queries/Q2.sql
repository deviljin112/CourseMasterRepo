use Northwind;

select 
    MAX(UnitPrice) as 'Most Expensive',
    MIN(UnitPrice) as 'Cheapest',
    AVG(UnitPrice) as 'Average Price'
from Products