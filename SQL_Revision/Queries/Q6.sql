use Northwind;

select
    CustomerID,
    CompanyName,
    ContactName,
    Phone,
    City
from Customers
where Country = 'UK'