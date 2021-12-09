use Northwind;

select
    Orders.OrderID,
    Orders.CustomerID,
    Employees.FirstName + ' ' + Employees.LastName as 'Employee Full Name',
    Orders.ShipCity
from Orders
inner join Employees on Orders.EmployeeID = Employees.EmployeeID
where Orders.ShipCountry = 'UK'
