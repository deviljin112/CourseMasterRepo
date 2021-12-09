use Northwind;

select
    ProductID,
    ProductName,
    UnitPrice,
    case
        when Discontinued = 1 then 'Discontinued'
        when Discontinued = 0 then 'Available'
        end as 'Discontinued'
from Products