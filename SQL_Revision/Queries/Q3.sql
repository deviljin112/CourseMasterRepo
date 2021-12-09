use Northwind;

select
    ProductID,
    ProductName,
    UnitPrice,
    Discontinued
from Products
where UnitPrice < 25