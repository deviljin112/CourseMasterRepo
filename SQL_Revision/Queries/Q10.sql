use Northwind;

select
    Orders.OrderID,
    Products.ProductName,
    Categories.CategoryName,
    Customers.CompanyName,
    Employees.FirstName + ' ' + Employees.LastName as 'Employee Full Name',
    DATEDIFF(yy, Employees.BirthDate, GETDATE()) as 'Employee Age',
    Products.UnitPrice,
    [Order Details].[Quantity],
    case
        when Orders.ShippedDate - Orders.RequiredDate > 0 then 'LATE'
        else 'ON TIME'
        end
        as 'Shipping Time'

from Orders
inner join [Order Details] on Orders.OrderID = [Order Details].OrderID
inner join Products on [Order Details].ProductID = Products.ProductID
inner join Customers on Orders.CustomerID = Customers.CustomerID
inner join Employees on Orders.EmployeeID = Employees.EmployeeID
inner join Categories on Products.CategoryID = Categories.CategoryID
