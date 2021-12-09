use Northwind;

select
    Orders.OrderID,
    Products.ProductName,
    Customers.CompanyName,
    Employees.FirstName + ' ' + Employees.LastName as 'Employee Full Name',
    Products.UnitPrice,
    [Order Details].[Quantity]
from Orders
inner join [Order Details] on Orders.OrderID = [Order Details].OrderID
inner join Products on [Order Details].ProductID = Products.ProductID
inner join Customers on Orders.CustomerID = Customers.CustomerID
inner join Employees on Orders.EmployeeID = Employees.EmployeeID