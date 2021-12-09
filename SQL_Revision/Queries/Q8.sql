use Northwind;

select
    Products.ProductID,
    Products.ProductName,
    Categories.CategoryName,
    Products.UnitPrice
from Products
inner join Categories on Products.CategoryID = Categories.CategoryID